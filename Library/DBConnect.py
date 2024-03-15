import pyodbc
from Values.constant import *

'''
    ================================================
    CONNECT AND EXECUTE SQL SERVER
    ================================================
    sample delete query:
    "SELECT * FROM Table Where columnname='abc' "
    "Delete from Employee Where FIRST_NAME = 'a' "
    "Update Employee Set FIRST_NAME = 'abc' Where age =19 "
    "Insert into Employee (FirstName, LastName) Values('a', 'b')"
'''
def exe_sql_query(statement):
    try:
        conn = pyodbc.connect(f"Driver={DRIVER_NAME};"
                              f"Server={SERVER_NAME};"
                              f"Database={DB_NAME};"
                              "Trusted_Connection=yes;")
        cursor = conn.cursor()
        cursor.execute(statement)
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()


