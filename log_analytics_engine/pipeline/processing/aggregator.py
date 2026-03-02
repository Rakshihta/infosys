import pandas as pd
import dask.dataframe as dd
import logging

logger = logging.getLogger(__name__)

def analyze(structured_logs: list[dict]) -> dd.DataFrame:
    
    df = dd.from_pandas(pd.DataFrame(structured_logs), npartitions=3)
    
    level_counts = df.groupby(df["Level"]).size().compute()
    service_counts = df.groupby(df["Service Name"]).size().compute()
    
    # log the results
    logger.info(f"Level counts:\n{level_counts}")
    logger.info(f"Service counts:\n{service_counts}")
    
    return df

