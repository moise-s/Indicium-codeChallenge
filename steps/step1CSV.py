import pandas as pd
from pathlib import Path


def csvToLocal(userDate):
    backup_dir = r"./data/CSV/{}/{}.csv"  # backup directory

    csv_table = pd.read_csv("./data/order_details.csv")

    path_to_store_table = Path(f"data/CSV/{userDate}")
    path_to_store_table.mkdir(parents=True, exist_ok=True)

    csv_table.to_csv(backup_dir.format(userDate, userDate))
