import requests

API_KEY = "8f58ed60f5ff89d02df91d1b8631b2a8"


def get_data(place, forecast_days=None, type_=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="tokyo"))
