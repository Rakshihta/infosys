import dask.dataframe as dd
import pandas as pd
import ray

print("\nStarting Dask + Ray log test...\n")

#fake logs
logs = [
    {"timestamp": "2026-02-15 20:00:00", "level": "ERROR", "message": "Code not found"},
    {"timestamp": "2026-02-15 20:01:00", "level": "ERROR", "message": "Code not found"},
    {"timestamp": "2026-02-15 20:02:00", "level": "ERROR", "message": "Code not found"},
    {"timestamp": "2026-02-15 20:03:00", "level": "INFO", "message": "Service started"},
]

df = pd.DataFrame(logs)

#process logs
dask_df = dd.from_pandas(df, npartitions=2)

error_count = dask_df[dask_df["level"] == "ERROR"].shape[0].compute()

print("Total ERROR logs (processed by Dask):", error_count)

#Ray - to check anomaly
ray.init(ignore_reinit_error=True)

@ray.remote
def check_anomaly(count):
    if count >= 3:
        return "ANOMALY DETECTED: Error spike!"
    return "System normal."

result = ray.get(check_anomaly.remote(error_count))

print("Ray Anomaly Check Result:", result)

ray.shutdown()

print("\nDask + Ray test completed successfully!")



# print("Checking Dask and Ray installation...\n")

# # Check Dask
# try:
#     import dask
#     print("Dask is installed successfully!")
# except ImportError:
#     print("Dask is NOT installed.")

# # Check Ray
# try:
#     import ray
#     ray.init(ignore_reinit_error=True)
#     print("Ray is installed and initialized successfully!")
#     ray.shutdown()
# except ImportError:
#     print("Ray is NOT installed.")
# except Exception as e:
#     print("Ray failed to initialize:", e)

# print("\nEnvironment check complete!")