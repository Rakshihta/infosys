# import ray
# from pprint import pprint
# from simulate.log_generator import generate_logs
# from pipeline.ingestion.ingestion import ingest_logs
# from pipeline.processing.processor import process_logs
# from pipeline.processing.aggregator import analyze
# from pipeline.processing.aggregator import store_logs
# from pipeline.anomaly.detector import detect_zscore
# from pipeline.alerts.notifier import send_email_alert

# if __name__ == "__main__":
#     ray.init()
    
#     lines = generate_logs(1000)
    
#     # step 2 - process
#     structured_logs = process_logs(lines)

#     # store logs into json file
#     store_logs(structured_logs, "output_logs.json")

#     # step 3 - analyze
#     df = analyze(structured_logs)

#     # step 4 - detect anomalies
#     anomalies = detect_zscore(structured_logs)
#     # pprint(anomalies)


#     #step 5 - email alert
#     send_email_alert(
#         anomalies=anomalies,
#         sender="rakshithad410@gmail.com",
#         password="usjb gnhb cszx mnbb",
#         recipient="rakshithad410@gmail.com"
#     )


from dotenv import load_dotenv
import os
from simulate.streaming import start_stream

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("RECIPIENT_EMAIL")

start_stream(
    window_size=100,
    sender=sender,
    password=password,
    recipient=recipient
)