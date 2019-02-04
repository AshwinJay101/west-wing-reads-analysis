from bs4 import BeautifulSoup
import pandas as pd
import requests
from multiprocessing import Pool


p = Pool(4)

def get_text(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content)
    para_list = soup.find_all('p')
    return (url, " ".join([x.get_text() for x in para_list]))


p = Pool(5)
df = pd.read_csv('west_wing_reads.csv')

p.map(get_text, list(df['link']))


url_list = df['link']

word_list = {}

cnt = 0
for url in url_list:
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.content)
        para_list = soup.find_all('p')
        word_list[url] = " ".join([x.get_text() for x in para_list])
        print(cnt)
        cnt += 1
    except Exception as e:
        word_list[url] = "Error"
        print(e)
        cnt += 1


words = pd.DataFrame(word_list.items(), columns=['url', 'text'])

words.to_csv('Words.csv', sep='|')