import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# date = 
url = f'https://pleagueofficial.com/stat-player/2022-23/2#record'


# 模仿使用者使用發出一個請求到伺服器端請求網頁
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

data = [th.text.strip('\n').split() for th in soup.find_all('tr')]
# print(data)