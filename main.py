from args import get_args
import pandas as pd
import args
from torch.utils.data import DataLoader
import os
from dataset import ObjDetectionDataset


def main():
    args = get_args()

    # 1. read the dataframes
    train_df = pd.read_csv(os.path.join(args.csv_dir, "train_df.csv"))
    val_df = pd.read_csv(os.path.join(args.csv_dir, "val_df.csv"))

    # 2. create datasets
    train_dataset = ObjDetectionDataset(train_df)
    val_dataset = ObjDetectionDataset(val_df)

    # 3. create dataloaders
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=False)

    print("DataLoaders created successfully")


if __name__ == "__main__":
    main()