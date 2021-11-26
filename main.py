import cx_Oracle
import login
import logging as log


class DB:
    def __init__(self, host):
        self.conn = cx_Oracle.connect(host)
        self.cur = self.conn.cursor()
        print(self.conn.version)

    def execute_query(self, query):
        sql_query = query
        self.cur.execute(sql_query)

    def print_query(self):
        for line in self.cur:
            print(line)
        self.cur.close()
        self.conn.close()


p1 = DB('c##scott/tiger@//192.168.0.6:1521/magazynw')
p1.execute_query("""SELECT * FROM CZESC""")
p1.print_query()

