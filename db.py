import sqlite3
import json

'''
============================================================================
Class: DB
Description: Responsável por criar base de dados para o SQLITE, criar tabela,
            gerar insert de dados, buscar dados.
Params: args=data
Autor: Igor Silva
Date: 25/10/2022
Updates: 
===============================================================================
'''


class DB:

    def __init__(self):
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
        data_json = json.load(open('out.json'))
        columns = ['id', 'track_name', 'size_bytes', 'prime_genre', 'n_citacoes']

        for row in data_json:
            keys = tuple(row[c] for c in columns)
            print(keys)
            self.cur.execute('INSERT INTO applestore VALUES(?, ?, ?, ?, ?)', keys)
            print(f'{row["id"]} dados inseridos com Sucesso!')

        self.con.commit()
        self.con.close()

    def selectAll(self):
        self.cur.execute('select * from applestore')
        data = self.cur.fetchall()
        self.con.commit()
        self.con.close()
        print(data)


    def main(self):
        self.insertData()
        self.selectAll()


if __name__ == '__main__':
    insert_data = DB()
    insert_data.main()
