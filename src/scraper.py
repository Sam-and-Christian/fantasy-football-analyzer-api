"""
scraper.py runs the web scraping function to pull in historical player/team stats
"""

from os import wait
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from models.stats import PlayerStats as s

# url = 'https://www.pro-football-reference.com/players/W/WilsRu00/fantasy/2018/'
# df = pd.read_html(url)[0]
# df.to_csv('test_RW_2018.csv')
# print('Saving to .csv ...')
# print(df)
# print('.csv saved.')

url = 'https://www.pro-football-reference.com'
year = 2021
maxp = 1
    
# grab fantasy players
r = requests.get(url + '/years/' + str(year) + '/fantasy.htm')
soup = BeautifulSoup(r.content, 'html.parser')
parsed_table = soup.find_all('table')[0]

df = []

# first 2 rows are col headers
for i,row in enumerate(parsed_table.find_all('tr')[2:]):
    if i >= maxp: 
        print('\nComplete.')
        break
        
    try:
        dat = row.find('td', attrs={'data-stat': 'player'})
        name = dat.a.get_text()
        stub = dat.a.get('href')
        stub = stub[:-4] + '/fantasy/' + str(year)
        pos = row.find('td', attrs={'data-stat': 'fantasy_pos'}).get_text()

        # grab this players stats
        print(f'Grabbing stats for {name}, {pos}')
        tdf = pd.read_html(url + stub)[0]    

        # get rid of MultiIndex, just keep last row
        tdf.columns = tdf.columns.get_level_values(-1)

        # fix the away/home column
        tdf = tdf.rename(columns={'Unnamed: 4_level_2': 'Away'})
        tdf['Away'] = [1 if r=='@' else 0 for r in tdf['Away']]

        # Rename RB columns
        # if pos == 'RB':
        #     tdf = tdf.rename(columns={tdf.columns[9]: 'Rush Att'})
        # # print(tdf.columns)
        # print(tdf)

        # drop all intermediate stats
        tdf = tdf.iloc[:,[1,2,3,4,5,-3]]
        
        # drop "Total" row
        tdf = tdf.query('Date != "Total"')
        
        # add other info
        tdf['Name'] = name
        tdf['Position'] = pos
        tdf['Season'] = year
        # stats = Stats(year=year, pos=pos)
        # df = df.reset_index()
        df.append(tdf)
    except:
        pass
    
df = pd.concat(df)
df.head()

csv_name = 'test_' + str(year) + '.csv'
print(f'\nCreating {csv_name}')
time.sleep(1)
df.to_csv(csv_name)
print('Saving .csv')
time.sleep(1.5)
print('...')
time.sleep(1.5)
print(f'{csv_name} saved.\n')
time.sleep(0.5)