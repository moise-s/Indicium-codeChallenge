# imports ------------------
from datetime import date
from steps import step1PG
from steps import step1CSV
from steps import step2toDB
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
    print("Step 1 - Postgress - FINISHED")


def step1CSVFile():  # step 1 for CSV
    userDate = getdate()
    step1CSV.csvToLocal(userDate)
    print("Step 1 - CSV - FINISHED")


def step2DB():  # step 2
    step2toDB.localToDB()
    print("Step 2 - FINISHED")
# --------------------------


# constants ----------------
MENU_OPTIONS = """
Choose an option from below:
    [1] STEP 1 (Postgress).
    [2] STEP 1 (CSV).
    [3] STEP 2.
    [4] Exit program.
Option: """

OPTIONS = {
    "1": step1Post,
    "2": step1CSVFile,
    "3": step2DB,
}
# --------------------------

# program running! ---------
if __name__ == "__main__":
    while(True):
        print("Welcome to my code_challenge_solution!")
        selectedOption = input(MENU_OPTIONS)
        if selectedOption == "4":
            print("\nThanks for using the program!")
            break
        try:
            OPTIONS[selectedOption]()
        except KeyError:
            print("\nThis is not a valid option!")
# --------------------------
