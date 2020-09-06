from datetime import datetime
import os
from os import path
import platform


def get_file_attr(file_path: str, file_name: str) -> dict:
    file_ = path.join(file_path, file_name)
    file_attrs = {}
    stat = os.stat(file_)
    file_attrs['name'] = file_name
    if platform.system() == 'Windows':
        file_attrs['ctime'] = datetime.fromtimestamp(path.getctime(file_))
    else:
        try:
            file_attrs['ctime'] = datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            file_attrs['ctime'] = datetime.fromtimestamp(stat.st_mtime)
    file_attrs['mtime'] = datetime.fromtimestamp(stat.st_mtime)
    return file_attrs


def create_list_files(path_to_dir: str, date=None) -> list:
    list_files = []
    list_files_ = os.listdir(path_to_dir)
    if date:
        for file_name in list_files_:
            file = get_file_attr(path_to_dir, file_name)
            if file['ctime'].date() == date.date():
                list_files.append(file)
        return list_files
    else:
        for file_name in list_files_:
            list_files.append(get_file_attr(path_to_dir, file_name))
        return list_files


def read_file_to_context(path_to_file: str) -> str:
    with open(path_to_file) as content_file:
        reader = content_file.read()
    return reader
