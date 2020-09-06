import csv


def read_bus_station(file_name: str) -> list:
    with open(file_name, encoding='cp1251') as csv_file:
        list_stations = list(csv.DictReader(csv_file, delimiter=','))
    return list_stations
