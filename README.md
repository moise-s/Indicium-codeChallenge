# Processo Seletivo - Lighthouse Programa De Formação Em Dados (Remoto) - Moisés.

## Data Engineer

- The **first section** of this file contains the instructions for running the program;
- The **second section** explicits some key info on my codes and decisions;
- The **third section** refers to a copy of Indicium instructions.

## **First Section:** _instructions_

This code challenge was solved using `python` language. Please make sure you have it installed in your environment.

Clone the repository to a folder of your choice:

```
git clone https://github.com/moise-s/Indicium-codeChallenge.git
```

Go to the repository folder, then install system requirements:

```
pip install requirements.txt
```

With docker properly installed, run the following:

```
docker-compose up
```

Check if both images are running (Postgres and MySQL).
Lastly, run the python main code:

```
python main.py
```

## **Second Section:** _my code_

My solution is contained of a `main.py` file, which properly runs the menu and calls the steps of challenge and communication with server in separate files.
The acessory files for running the whole program are:

`step1CSV.py` using _pandas_ to run `read_csv()` and paste content into new path and file through`to_csv()` instruction;

`step1PG.py` now a connection with Postgres DB is needed, so library _psycopg2_ was used. Also, _pandas_ was needed to read SQL content, convert to CSV and create new paths and files;

`conn.py` runs communication with MySQL server (database chosen for Step 2 of this project) through _sqlalchemy_ library;

`step2toDB.py` connects to MySQL server through `conn.py`, and using _pandas_, the data from new files of step 1 is written to MySQL server.

### Files generated on Step 1

The format and path of files are as follows:

```
/data/POSTGRES/{table_name}/{userDate}/{userDate}.csv
/data/CSV/{userDate}/{userDate}.csv
```

### Program flow

When running `main.py`, the following menu options will appear:

```
Choose an option from below:
    [1] STEP 1 (Postgress).
    [2] STEP 1 (CSV).
    [3] STEP 2.
    [4] Query test PRODUCTS.
    [5] Query test ORDER_DETAILS.
    [6] Exit program.
```

So, due to Indicium's requirements, **in the first moment**, it is only possible to run commands `1` and `2`, otherwise a message will be displayed.
After step 1 is complete for a specific date, it is possible to run step 2 of the same date, running command `3` on menu.

#### **Example:** if you want to run date `2022-01-01`, it is necessary to choose options `1` and `2` from menu using this date, and then choose option `3` with same date to sucessfully run step 2.

After running option `3` of the menu, it is possible to run sample queries, choosing options `4` and `5`.

To exit program, just choose option `6`.

### Needed improvements

- Provide error messages when some step was not successful.
- Improve my knowledge in good practices of coding.

## **Third Section:** _instructions from Indicium_

### code-challenge

Indicium code challenge for Software Developer focusing on data projects

### Indicium Tech Code Challenge

Code challenge for Software Developer with focus in data projects.

#### Context

At Indicium we have many projects where we develop the whole data pipeline for our client, from extracting data from many data sources to loading this data at its final destination, with this final destination varying from a data warehouse for a Business Intelligency tool to an api for integrating with third party systems.

As a software developer with focus in data projects your mission is to plan, develop, deploy, and maintain a data pipeline.

#### The Challenge

We are going to provide 2 data sources, a Postgres database and a CSV file.

The CSV file represents details of orders from a ecommerce system.

The database provided is a sample database provided by microsoft for education purposes called northwind, the only difference is that the order_detail table does not exists in this database you are beeing provided with.This order_details table is represented by the CSV file we provide.

Schema of the original Northwind Database:

![image](https://user-images.githubusercontent.com/49417424/105997621-9666b980-608a-11eb-86fd-db6b44ece02a.png)

Your mission is to build a pipeline that extracts the data everyday from both sources and write the data first to local disk, and second to a database of your choice. For this challenge, the CSV file and the database will be static, but in any real world project, both data sources would be changing constantly.

Its important that all writing steps are isolated from each other, you shoud be able to run any step without executing the others.

For the first step, where you write data to local disk, you should write one file for each table and one file for the input CSV file. This pipeline will run everyday, so there should be a separation in the file paths you will create for each source(CSV or Postgres), table and execution day combination, e.g.:

```
/data/postgres/{table}/2021-01-01/file.format
/data/postgres/{table}/2021-01-02/file.format
/data/csv/2021-01-02/file.format
```

you are free to chose the naming and the format of the file you are going to save.

At step 2, you should load the data from the local filesystem to the final database that you chosed.

The final goal is to be able to run a query that shows the orders and its details. The Orders are placed in a table called **orders** at the postgres Northwind database. The details are placed at the csv file provided, and each line has an **order_id** field pointing the **orders** table.

How you are going to build this query will heavily depend on which database you choose and how you will load the data this database.

The pipeline will look something like this:

![image](https://user-images.githubusercontent.com/49417424/105993225-e2aefb00-6084-11eb-96af-3ec3716b151a.png)

#### Requirements

- All tasks should be idempotent, you should be able the whole pipeline for a day and the result should be always the same
- Step 2 depends on both tasks of step 1, so you should not be able to run step 2 for a day if the tasks from step 1 did not succeed
- You should extract all the tables from the source database, it does not matter that you will not use most of them for the final step.
- You should be able to tell where the pipeline failed clearly, so you know from which step you should rerun the pipeline
- You have to provide clear instructions on how to run the whole pipeline. The easier the better.
- You have to provide a csv or json file with the result of the final query at the final database.
- You dont have to actually schedule the pipeline, but you should assume that it will run for different days.
- Your pipeline should be prepared to run for past days, meaning you should be able to pass an argument to the pipeline with a day from the past, and it should reprocess the data for that day. Since the data for this challenge is static, the only difference for each day of execution will be the output paths.

#### Things that Matters

- Clean and organized code.
- Good decisions at which step (which database, which file format..) and good arguments to back those decisions up.

#### Setup of the source database

The source database can be set up using docker compose.
You can install following the instructions at
https://docs.docker.com/compose/install/

With docker compose installed simply run

```
docker-compose up
```

You can find the credentials at the docker-compose.yml file

#### Final Instruction

You can use any language you like, but keep in mind that we will have to run your pipeline, so choosing some languague or tooling that requires a complex environment might not be a good idea.
You are free to use opensource libs and frameworks, but also keep in mind that **you have to write code**. Point and click tools are not allowed.

Thank you for participating!
