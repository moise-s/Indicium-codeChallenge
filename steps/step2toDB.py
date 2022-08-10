import pandas as pd
import os
from sqlalchemy import create_engine
from conn import conn


def localToDB():

    engine = conn.connMySql()
    rootDirPos = r"./data/POSTGRES/"
    for dirName, subdirList, fileList in os.walk(rootDirPos, topdown=False):
        for fname in fileList:
            filepath = os.path.join(dirName, fname)
            table_name = filepath.split("\\")[-3].split('/')[-1]
            df = pd.read_csv(filepath)
            df.to_sql(table_name, con=engine,
                      index=False, if_exists="replace")
            print(f"{filepath} written successfully")

    rootDirCSV = r"./data/CSV/"
    for dirName, subdirList, fileList in os.walk(rootDirCSV, topdown=False):
        for fname in fileList:
            filepath = os.path.join(dirName, fname)
            table_name = 'order_details'
            df = pd.read_csv(filepath)
            df.to_sql(table_name, con=engine,
                      index=False, if_exists="replace")
            print(f"{filepath} written successfully")

    orders = pd.read_sql("SELECT * FROM orders", con=engine)
    details = pd.read_sql("SELECT * FROM order_details", engine)
