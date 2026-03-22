import time
import logging
import ray
from simulate.log_generator import generate_log
from pipeline.processing.parse import parse_log
from pipeline.anomaly.detector import detect_zscore
from pipeline.alerts.notifier import send_email_alert

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_stream(window_size: int = 100,
                 sender: str = "",
                 password: str = "",
                 recipient: str = "") -> None:
    
    window = []
    total_processed = 0
    total_anomalies = 0
    
    logger.info("Starting real-time log stream...")
    
    while True:
        # step 1 - generate one log
        raw_log = generate_log(anomaly=False if __import__('random').random() > 0.1 else True)
        
        # step 2 - parse it using ray
        parsed = ray.get(parse_log.remote(raw_log))
        
        # step 3 - add to window if valid
        if parsed:
            window.append(parsed)
            total_processed += 1
        
        # step 4 - if window is full, analyze and detect
        if len(window) >= window_size:
            logger.info(f"Analyzing window of {window_size} logs...")
            
            anomalies = detect_zscore(window)
            
            if anomalies:
                total_anomalies += len(anomalies)
                logger.warning(f"{len(anomalies)} anomalies detected!")
                
                send_email_alert(
                    anomalies=anomalies,
                    sender=sender,
                    password=password,
                    recipient=recipient
                )
            else:
                logger.info("No anomalies in this window")
            
            logger.info(f"Total processed: {total_processed} | Total anomalies: {total_anomalies}")
            
            # reset window
            window = []
        
        # step 5 - small delay to simulate real time
        time.sleep(0.01)