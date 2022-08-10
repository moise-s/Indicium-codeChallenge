import pandas as pd
import psycopg2
from pathlib import Path


def postgresToLocal(userDate):
    backup_dir = r"./data/POSTGRES/{}/{}/{}.csv"
    conn = psycopg2.connect(
        dbname="northwind", user="northwind_user", password="thewindisblowing")
    cur = conn.cursor()
    cur.execute(
        "SELECT table_schema, table_name FROM information_schema.tables WHERE( table_schema = 'public') ORDER BY table_schema, table_name;"
    )
    list_tables = cur.fetchall()
    for t_name_table in list_tables:
        table_name = t_name_table[1]
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

        path_to_store_table = Path(
            f"data/POSTGRES/{table_name}/{userDate}")
        path_to_store_table.mkdir(parents=True, exist_ok=True)
        df.to_csv(backup_dir.format(table_name, userDate, userDate))
