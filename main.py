import cx_Oracle

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


#p1 = DB('c##scott/tiger@//192.168.0.137:1521/orcl1')
#p1.execute_query("""SELECT * FROM KLENCI1""")
#p1.print_query()

