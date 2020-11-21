import pyodbc
import ConnectionTest as connBase

cursor = connBase.conn.cursor()


# sqlCmd = "INSERT INTO customers(name,address) VALUES('Alireza2','N51 196'),('BEHNAZ3','N52 196')"
# try:
#     result = cursor.execute(sqlCmd)
#     result = str(cursor.rowcount) + ' row(s) affected!'
# except pyodbc.Error as ex:
#     result = 'This Error raised: '+str(ex)


# sql = "INSERT INTO customers (name, address) VALUES "
# val = "('Peter', 'Lowstreet 4'), ('Amy', 'Apple st 652'), ('Hannah', 'Mountain 21'), ('Michael', 'Valley 345'), ('Sandy', 'Ocean blvd 2'), ('Betty', 'Green Grass 1'), ('Richard', 'Sky st 331'), ('Susan', 'One way 98'), ('Vicky', 'Yellow Garden 2'), ('Ben', 'Park Lane 38'), ('William', 'Central st 954'), ('Chuck', 'Main Road 989'), ('Viola', 'Sideway 1633')"
# sql += val
# print(sql)


# sql = "DELETE customers WHERE name='Ben'"
# try:
#     result = cursor.execute(sql)
#     result = str(cursor.rowcount) + ' row(s) deleted!'
# except pyodbc.Error as ex:
#     result = 'This Error raised: '+str(ex)


# print(result)
