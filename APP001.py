import pandas as pd

data = pd.read_csv(r'AppleStore.csv', sep=',', encoding='ISO-8859-1', index_col=False)


def report_gen(data_table):
    data_table.columns = [column.replace(" ", "_") for column in data_table.columns]
    data_table.query('prime_genre == "Music" or prime_genre == "Book"', inplace=True)
    data_table = data_table[['id', 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']]

    top10 = data_table[['id', 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']][:10].sort_values(
        by='rating_count_tot', ascending=False)

    frequency = top10['prime_genre'].value_counts()
    top10['n_citacoes'] = str(frequency['Music'] if frequency['Music'] else frequency['Book'])
    top10.to_csv('out.csv', sep=',', index=False)
    top10.to_json(r'out.json', orient="index")
    print(top10)

    #print(str(frequency['Music'] if frequency['Music'] > frequency['Book'] else frequency['Book']))


def report_news(data_table):
    # Substituo espaços por '_'
    data_table.columns = [column.replace(" ", "_") for column in data.columns]

    # Execute filtrates
    data_table.query('prime_genre == "News"', inplace=True)

    max_news = data_table['rating_count_tot'].max()
    track_name = data_table.loc[data_table['rating_count_tot'] == max_news, 'track_name'].values[0]

    data_table[['id', 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']][:10].sort_values(
        by='rating_count_tot', ascending=False)

    # print(max_News)
    # print(track_Name)

    print(
        f'Aplicação da categoria News com maior quantidade de avaliações: {max_news} | Total de avaliações de {track_name}')


# report_News(data)
report_gen(data)
'''
if (tabela['prime_genre'] == 'News').any():
    print(tabela.loc[tabela['prime_genre'] == 'News', 'prime_genre'].values[0])
    print(tabela['prime_genre'].count())
    print(tabela['rating_count_tot'].max())
    '''
