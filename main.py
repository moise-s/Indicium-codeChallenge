# imports ------------------
from steps import step1PG
from steps import step1CSV
from steps import step2toDB
from conn import conn
from os import path
from datetime import date
import pandas as pd
# --------------------------

# functions ----------------


def getdate():  # Get user date for program running
    today = date.today().isoformat()
    WRITE_DATE = f"Write down desired date for program running (Note: yyyy-mm-dd format. Default {today}): "
    userDate = input(WRITE_DATE)
    if userDate == '':
        return today
    try:
        userDate = date.fromisoformat(userDate)
    except ValueError:
        print("Your entry is invalid, using today's date instead!")
        userDate = today
    return userDate


def step1Post():  # step 1 for POSTGRESS
    userDate = getdate()
    step1PG.postgresToLocal(userDate)
    print("\nStep 1 - Postgress - FINISHED")


def step1CSVFile():  # step 1 for CSV
    userDate = getdate()
    step1CSV.csvToLocal(userDate)
    print("\nStep 1 - CSV - FINISHED")


flag = 0  # flag to block user from choosing queries before step 2


def step2DB():  # step 2
    global flag
    userDate = getdate()
    postExists = r"./data/POSTGRES/categories/{}"
    CSVExists = r"./data/CSV/{}"
    if (path.exists(postExists.format(userDate)) and path.exists(CSVExists.format(userDate))):
        step2toDB.localToDB()
        flag += 1
        print("\nStep 2 - FINISHED")
    else:
        print("\nPlease finish Step1 for POSTGRES and CSV files before entering Step 2")


def testQueryProd():
    if flag < 1:
        print("\nPlease finish Steps 1 and 2 before entering Queries")
    else:
        engine = conn.connMySql()
        products = pd.read_sql("SELECT * FROM products", con=engine)
        print("\nQuery: SELECT * FROM products")
        print(products)


def testQueryOrdDet():
    if flag < 1:
        print("\nPlease finish Steps 1 and 2 before entering Queries")
    else:
        engine = conn.connMySql()
        details = pd.read_sql("SELECT * FROM order_details", con=engine)
        print("\nQuery: SELECT * FROM order_details")
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
