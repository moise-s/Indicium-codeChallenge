from sqlalchemy import create_engine


def connMySql():
    user = 'user'
    password = 'password'
    host = 'localhost:3333'
    dbname = 'northwind_complete'
    dbengine = "mysql+pymysql://{}:{}@{}/{}".format(
        user, password, host, dbname)
    engine = create_engine(dbengine)
    return engine
