import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


url = f'https://pleagueofficial.com/standings/2020-21'
# 模仿使用者使用發出一個請求到伺服器端請求網頁
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# 排名標題
data = [th.text for th in soup.find_all('tr')]
print(data)
temp_header = data[0].split('\n')
header = temp_header[1:9]
print(header)

body = []
for i in range(1,5):
  temp_body = data[i].split('\n')
  temp_body = temp_body[1:9]
  body = body + [temp_body]

df = pd.DataFrame(body, columns=header)
print(df)