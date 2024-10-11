import requests

url = "https://apihub.kma.go.kr/api/typ01/url/gts_syn1.php"
params ={
    'tm': '202211301200',  # ex Date
    'dtm': '3',  # ex Val
    'stn': '47',  # ex Val (station num)
    'authKey': 'TAZXxBq0Q66GV8QatHOuqg'  # API key
}


response = requests.get(url, params=params)

# check response status
if response.status_code == 200:
    # save data as txt file
    with open("weather_data.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("successful!")
else:
    print(f"API request failed: {response.status_code}")
