import ConnectionTest as connBase

cursor = connBase.conn.cursor()

# result = cursor.execute(
#     'CREATE TABLE customers2 (name VARCHAR(255), address VARCHAR(255))')

# result = cursor.execute('DROP TABLE customers2')

# print(result)
# print(type(result))

cursor = connBase.conn.cursor()
cursor.execute('Select * from customers')


for row in cursor:
    print(row)
