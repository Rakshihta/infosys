import pandas as pd
import numpy as np

n = 1_000_000

data = {
    "id": np.arange(1, n + 1),
    "name": np.random.choice(["Alice", "Bob", "Charlie", "David", "Emma"], n),
    "age": np.random.randint(21, 60, n),
    "salary": np.random.randint(30000, 120000, n),
    "department": np.random.choice(["HR", "IT", "Finance", "Marketing"], n)
}

df = pd.DataFrame(data)
# print(df.head())
# print(df.count())


df.to_csv("dataset.csv",index=False)

import dask.dataframe as dd

ddf = dd.read_csv("dataset.csv")

print(ddf.head(10))
# print("running")
print(ddf.npartitions)





