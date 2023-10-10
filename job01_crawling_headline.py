from turtle import title

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

#news.naver.com

category = ['Politics', 'Economic', 'Social', 'Culture', 'world', 'IT']
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

df_titles = pd.DataFrame()
myheaders = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

resp = requests.get(url, headers = myheaders)
#print(type(resp))

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

title_tags = soup.select('.sh_text_headline')

print(str(title_tags[0]).split('>')[1].split('<')[0])
#print(type(title_tags[0]))

title = []
for title_tags in title_tags:
    title.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', title_tags.text))
    #title.append(title_tags.text)

print(title)
print(len(title))


df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z]')

#for i in range(6):
#    resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i), )
