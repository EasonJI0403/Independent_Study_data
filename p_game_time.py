import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

total = []

def cat(game_id):

  # game_id = 432
  url = f'https://pleagueofficial.com/game/{game_id}'
  # 模仿使用者使用發出一個請求到伺服器端請求網頁
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
  response = requests.get(url, headers=headers)
  # print(response.text)

  soup = BeautifulSoup(response.text, "html.parser")
  # soup

  # 球員數據標題欄
  player_data_header = soup.find("span", class_="fs14 text-white")
  # print(player_data_header.text)
  player_header_text = ",".join(player_data_header.stripped_strings)      # .strip() 功能為去除首尾空白字符
  player_data_header_list = player_header_text.split(",")
  del player_data_header_list[0]
  player_data_header_list.insert(0, f"G{game_id}")
  total.append(player_data_header_list)

for i in range(423, 517):
  cat(i)
# print(total)

df = pd.DataFrame(total)
df.to_csv(f'E:/final/p_single_data/game_time/p_single_game_time_2023-24_data.xlsx.csv', index=False, encoding='utf-8')
# df.to_excel(f"p_gametime_2023-24_data.xlsx", index=False, engine="openpyxl")
# print("g")