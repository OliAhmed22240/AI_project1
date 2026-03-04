import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/CSVs/dataset.csv")

train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

train_df.to_csv("data/CSVs/train_df.csv", index=False)
val_df.to_csv("data/CSVs/val_df.csv", index=False)

print("Split completed successfully")