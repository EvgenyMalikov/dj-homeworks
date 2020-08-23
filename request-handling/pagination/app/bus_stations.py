import csv


def read_bus_station(file_name: str) -> list:
    with open(file_name, encoding='cp1251') as csv_file:
        list_stations = list(csv.DictReader(csv_file, delimiter=','))
    return list_stations



from urllib.parse import urlencode

APP_ID = 6858171
AUTH_URL = 'https://oauth.vk.com/authorize'


aut_data = {
    'client_id': APP_ID,
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.92'
}

print('?'.join((AUTH_URL, urlencode(aut_data))))
