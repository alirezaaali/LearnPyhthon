import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-U3Q2COI\\SQLEXPRESS;'
    'DATABASE=pythontestdb;UID=sa;PWD=axim@95661;')

conn.autocommit = True
