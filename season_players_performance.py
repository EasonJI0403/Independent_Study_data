import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

date = '2022-23'
url = f'https://pleagueofficial.com/stat-player/{date}/2#record'


# 模仿使用者使用發出一個請求到伺服器端請求網頁
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# 球員數據標題欄
player_data_header = soup.find("thead", class_="bg-deepgray")
player_header_text = ",".join(player_data_header.stripped_strings)      # .strip() 功能為去除首尾空白字符
player_data_header_list = player_header_text.split(",")

# 球員數據
articles = soup.find_all("tbody")

player_data_list=[]
for a in articles:
  # 球員數據
  player_data_soup = a.find_all("tr")
  # print(player_data_soup)
  for player_data in player_data_soup:
    player_cleaned = [cleaned.strip() for cleaned in player_data.stripped_strings]
    player_data_list.append(player_cleaned)
player_data_list = np.array(player_data_list)

# 把 list 們串起來
total_player_data = {}
for i, header in enumerate(player_data_header_list):
    total_player_data[header] = player_data_list[:, i]


df = pd.DataFrame(total_player_data)
df.to_excel(f"p_plus_players{date}_data.xlsx", index=False, engine="openpyxl")
print("Saved successfully!")