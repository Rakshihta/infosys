import time
import logging
import ray
import json
from simulate.log_generator import generate_log
from pipeline.processing.parse import parse_log
from pipeline.anomaly.detector import detect_zscore
from pipeline.alerts.notifier import send_email_alert

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_anomalies(anomalies: list[dict], path: str = "anomalies.json") -> None:
    try:
        with open(path, "r") as f:
            existing = json.load(f)
    except:
        existing = []
    
    existing.extend(anomalies)
    
    with open(path, "w") as f:
        json.dump(existing, f, indent=4)

def save_logs(window: list[dict], path: str = "output_logs.json") -> None:
    try:
        with open(path, "r") as f:
            existing = json.load(f)
    except:
        existing = []
    
    existing.extend(window)
    
    with open(path, "w") as f:
        json.dump(existing, f, indent=4)

def start_stream(window_size: int = 100,
                 sender: str = "",
                 password: str = "",
                 recipient: str = "") -> None:
    
    window = []
    total_processed = 0
    total_anomalies = 0
    
    logger.info("Starting real-time log stream...")
    
    while True:
        raw_log = generate_log(anomaly=False if __import__('random').random() > 0.1 else True)
        parsed = ray.get(parse_log.remote(raw_log))
        
        if parsed:
            window.append(parsed)
            total_processed += 1
        
        if len(window) >= window_size:
            logger.info(f"Analyzing window of {window_size} logs...")
            save_logs(window) 
            anomalies = detect_zscore(window)
            
            if anomalies:
                total_anomalies += len(anomalies)
                logger.warning(f"{len(anomalies)} anomalies detected!")
                save_anomalies(anomalies)  # ← save to file
                send_email_alert(
                    anomalies=anomalies,
                    sender=sender,
                    password=password,
                    recipient=recipient
                )
            else:
                logger.info("No anomalies in this window")
            
            logger.info(f"Total processed: {total_processed} | Total anomalies: {total_anomalies}")
            window = []
        
        time.sleep(0.01)

