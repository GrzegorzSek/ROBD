import cx_Oracle

# create connection
conn = cx_Oracle.connect('c##scott/tiger@//192.168.0.6:1521/magazynw')
print(conn.version)


# create cursor
cur = conn.cursor()

sql_query = """ 
SELECT * FROM czesc WHERE nazwa = :proba
"""

cur.execute(sql_query, ["test1"])
for line in cur:
    print(line)
cur.close()
conn.close()
