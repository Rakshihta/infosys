import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ingest_logs(filepath: str) -> list[str]:
    try:
        lines = []
        with open(filepath, "r") as file:
            for line in file:
                lines.append(line)
            logger.info(f"Successfully ingested {len(lines)} lines from {filepath}")
        
        return lines
                
    except FileNotFoundError:
        logger.error("File does not exist")


# # import json

# # logs = []
# # with open(log_file,"r") as file:
# #     for line in file:
# #         line = line.strip()
# #         i = json.loads(line)
# #         logs.append(i)
    
# #     print(type(logs[0]))


# def create_batches(logs,batch_size):
#     batched_logs = []
#     for i in range(0,len(logs),batch_size):
#         batched_logs.append(logs[i:i + batch_size])
    
#     for index, batch in enumerate(batched_logs):
#         print("Batch", index, "size:", len(batch))

#     return batched_logs 


# @ray.remote
# def parse_log(line):
#     line = line.strip()
#     if not line or " " not in line:
#         return None

#     left_part, timestamp = line.rsplit(" ", 1)
#     fields = left_part.split(" ",3)
    
#     return {
#         "Level" : fields[0],
#         "Service Name" : fields[1],
#         "Status_code" : int(fields[2]),
#         "message" : fields[3],
#         "timestamp" : timestamp
#     }

# log_file = "sample_logs.txt"
# future = []
# with open(log_file,"r") as file:
#     for line in file:
#         future.append(parse_log.remote(line))
    

# results = ray.get(future)
# structured_logs = [r for r in results if r is not None]
# print(structured_logs)    
# df = dd.from_pandas(pd.DataFrame(structured_logs), npartitions=3)
# level_counts = df.groupby(df["Level"]).size().compute()
# service_counts = df.groupby(df["Service Name"]).size().compute()
# print(level_counts)
# print(service_counts)






