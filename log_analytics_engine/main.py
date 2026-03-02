import ray
from pipeline.ingestion.ingestion import ingest_logs
from pipeline.processing.processor import process_logs
from pipeline.processing.aggregator import analyze

if __name__ == "__main__":
    ray.init()
    
    # step 1 - ingest
    lines = ingest_logs("log_analytics_engine/sample_logs.txt")
    
    # step 2 - process
    structured_logs = process_logs(lines)
    
    # step 3 - analyze
    df = analyze(structured_logs)