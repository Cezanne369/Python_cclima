#type: ignore
import requests
import pandas as pd
from datetime import datetime
from api import *

resquest = requests.get(URL)
data = resquest.json()

registration = {
    'date_hours': datetime.now().strftime('%y-%m-%d %H:%M:%S'),
    'city': CIDADE,
    'temperature': data['main']['temp'],
    'thermal sensation':data['main']['feels_like'],
    'weather': data['weather'][0]['description'],
    'humidity': data['main']['humidity'],
    'wind': data['wind']['speed'] * 3.6
}

file = 'weather forecast.csv'

try:
    df_old = pd.read_csv(file)
    df_new = pd.concat([df_old, pd.DataFrame([registration])])
except FileNotFoundError:
    df_new =pd.DataFrame([registration])

df_new.to_csv(file, index=False)
print("!Arquivo salvo com sucesso!")

