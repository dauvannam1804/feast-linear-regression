import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

df = pd.read_csv("engaged_polliwog/feature_repo/data/Advertising.csv").drop(columns=["Unnamed: 0"], errors="ignore")

df = df.reset_index().rename(columns={"index":"ad_id"})

start = datetime.now()
df["event_timestamp"] = [start + timedelta(minutes=int(i)) for i in df["ad_id"]]

os.makedirs("engaged_polliwog/feature_repo/data", exist_ok=True)
df.to_parquet("engaged_polliwog/feature_repo/data/Advertising.parquet", index=False)

print("Saved engaged_polliwog/feature_repo/data/Advertising.parquet with columns:", df.columns.tolist())