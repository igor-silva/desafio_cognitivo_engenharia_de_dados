import sqlite3

class DB:
    def __init__(self, args):
        self.data = args
        self.con = sqlite3.connect("cognitivoDB.db")
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS applestore("
                         " id integer, "
                         " track_name text,"
                         " size_bytes integer,"
                         " prime_genre text,"
                         " n_citacoes integer"
                         ")"
                         )
    def insertData(self):
        self.create_table()
        self.cur.executemany("INSERT INTO applestore VALUES(?, ?, ?, ?, ?)",  self.data)
        self.con.commit()

    def selectAll(self):
        self.cur.execute('select * from applestore')
        data = self.cur.fetchall()
        print(data)

    def main(self):
        self.insertData()
        self.selectAll()

if __name__ == '__main__':
    data = [
        (1, 'teste', 200, 'Music', 22),
    ]

    db = DB(data).main()