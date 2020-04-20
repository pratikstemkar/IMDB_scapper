import sys
from bs4 import BeautifulSoup
from tqdm import tqdm
import datetime
import requests
import os

headers = {'User-agent': 'Mozilla/5.0'}
current_year = int(datetime.datetime.now().year)
input_year = int(input("Please enter start year: "))
if input_year > current_year:
    print("No movie is recorded for the year %i!!" % (input_year))
else:
    for year in tqdm(range(input_year, current_year+1)):
        url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find('div', attrs={'class': 'article'}).find('h1')
        print(article.contents[0] + ': ')
        lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
        i = 1
        movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
        for div_item in tqdm(movieList):
            div = div_item.find('div', attrs={'class': 'lister-item-content'})
            print(str(i) + '.',)
            header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
            print('Movie:' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
            i += 1
