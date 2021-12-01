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



#p1 = DB('c##scott/tiger@//192.168.0.8:1521/orcl1')
#part = "Nadkole"
#sql = "SELECT * FROM czesc_view WHERE '" + part + "' IN(czesc_nazwa, marka_nazwa, model_nazwa)"
#print(sql)
#p1.execute_query("SELECT * FROM czesc_view WHERE 'Nadkole' IN(czesc_nazwa, marka_nazwa, model_nazwa)")
#p1.execute_query(sql)
#p1.cur.callproc("EXEC dodaj_czesc('Nadkole', 'Nadkole nowe', 1, 3, 2)")
#p1.print_query()

