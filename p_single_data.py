import requests
import pandas as pd

def single_game_data(game_id):
    parameters = {
    "id": game_id,
    'away_tab':'total',
    'home_tab':'total'
    }
    response = requests.get("https://pleagueofficial.com/api/boxscore.php?", params=parameters)

    # print(response.json())

    if response.status_code == 200:
        # 將 API 響應轉換為 JSON 格式
        json_data = response.json()
    # print(json_data['data'])

        # 將 JSON 數據轉換為 DataFrame
        df = pd.json_normalize(json_data['data']['home'])
        df.to_csv(f'E:/final/p_single_data/game23_24/game{game_id}.csv', index=False, encoding='utf-8')
        df = pd.json_normalize(json_data['data']['away'])
        df.to_csv(f'E:/final/p_single_data/game23_24/game{game_id}.csv', index=False, encoding='utf-8')

    else:
        print("Failed to fetch data from the API. Status code:", response.status_code)

    # print("Data has been successfully converted to CSV and saved.")

for i in range(423, 511):
    single_game_data(i)