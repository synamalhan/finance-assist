# fred_data.py
import requests
import pandas as pd

def fetch_fred_data(series_id,start_date='2000-01-01'):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        'series_id': series_id,
        'api_key': "0328c649ab34b6e310e1228c6ab73569",
        'file_type': 'json',
        'observation_start': start_date
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "observations" not in data:
        raise Exception("Error fetching data from FRED")

    df = pd.DataFrame(data['observations'])
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df


