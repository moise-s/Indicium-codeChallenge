# imports ------------------
from datetime import date
from steps import step1PG
from steps import step1CSV
from steps import step2toDB
import pandas as pd
from conn import conn
# --------------------------

# functions ----------------


def getdate():  # Get user date for program running
    today = date.today().isoformat()
    WRITE_DATE = f"Write down desired date for program running (Note: yyyy-mm-dd format. Default {today}): "
    userDate = input(WRITE_DATE)
    if userDate == '':
        return today
    userDate = date.fromisoformat(userDate)
    return userDate


def step1Post():  # step 1 for POSTGRESS
    userDate = getdate()
    step1PG.postgresToLocal(userDate)
    print("\nStep 1 - Postgress - FINISHED")


def step1CSVFile():  # step 1 for CSV
    userDate = getdate()
    step1CSV.csvToLocal(userDate)
    print("\nStep 1 - CSV - FINISHED")


def step2DB():  # step 2
    step2toDB.localToDB()
    print("\nStep 2 - FINISHED")


def testQueryProd():
    engine = conn.connMySql()
    products = pd.read_sql("SELECT * FROM products", con=engine)
    print(products)


def testQueryOrdDet():
    engine = conn.connMySql()
    details = pd.read_sql("SELECT * FROM order_details", con=engine)
    print(details)
# --------------------------


# constants ----------------
MENU_OPTIONS = """
Choose an option from below:
    [1] STEP 1 (Postgress).
    [2] STEP 1 (CSV).
    [3] STEP 2.
    [4] Query test PRODUCTS.
    [5] Query test ORDER_DETAILS.
    [6] Exit program.
Option: """

OPTIONS = {
    "1": step1Post,
    "2": step1CSVFile,
    "3": step2DB,
    "4": testQueryProd,
    "5": testQueryOrdDet,
}
# --------------------------

# program running! ---------
if __name__ == "__main__":
    print("\nWelcome to my code_challenge_solution!")
    while(True):
        selectedOption = input(MENU_OPTIONS)
        if selectedOption == "6":
            print("\nThanks for using the program!")
            break
        try:
            OPTIONS[selectedOption]()
        except KeyError:
            print("\nThis is not a valid option!")
# --------------------------
