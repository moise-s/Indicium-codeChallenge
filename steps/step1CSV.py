import pandas as pd
from pathlib import Path


def csvToLocal(userDate):
    csv_table = pd.read_csv("./data/order_details.csv")
    createDir = Path(f"data/CSV/{userDate}")
    createDir.mkdir(parents=True, exist_ok=True)
    finalDir = r"./data/CSV/{}/{}.csv"
    csv_table.to_csv(finalDir.format(userDate, userDate))
