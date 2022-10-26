import pandas as pd
from api_twiter import APITwiter
from db import DB

#Ler dados do arquivo CSV
data = pd.read_csv(r'AppleStore.csv', sep=',', encoding='ISO-8859-1', index_col=False)

'''
============================================================================
Function: report_gen
Description: Gerar reltório de dados estraídos de um arquivo CSV
Params: data_table
Autor: Igor Silva
Date: 25/10/2022
Updates: 
===============================================================================
'''
def report_gen(data_table):

    data_table.columns = [column.replace(" ", "_") for column in data_table.columns]
    data_table.query('prime_genre == "Music" or prime_genre == "Book"', inplace=True)
    data_table = data_table[['id', 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']]

    top10 = data_table[['id', 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']][:10].sort_values(
        by='rating_count_tot', ascending=False)

    #frequency = top10['prime_genre'].value_counts()
    #top10['n_citacoes'] = str(frequency['Music'] if frequency['Music'] else frequency['Book'])

    api_music = APITwiter('Music')
    data_music = api_music.main()
    count_music = len([x['title'] for x in data_music['data']])

    api_book = APITwiter('Book')
    data_book = api_book.main()
    count_book = len([x['title'] for x in data_book['data']])

    top10['n_citacoes'] = count_music + count_book

    top10.to_csv('out.csv', sep=',', index=False)
    top10.to_json(r'out.json', orient="records")

    #insert_data = DB()
    #insert_data.main()
   #print(top10)

report_gen(data)

if __name__ == '__main__':
    ...