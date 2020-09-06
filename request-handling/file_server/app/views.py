from .tools import create_list_files, read_file_to_context
from os import path

from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # context = {
    #     'files': [
    #         {'name': 'file1.txt',
    #          'ctime': datetime.datetime(2018, 1, 1),
    #          'mtime': datetime.datetime(2018, 1, 2)}
    #     ],
    #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    # }
    context = {
        'files': create_list_files(settings.FILES_PATH, date),
        'date': date.date() if date else ''
    }
    return render(request, template_name, context)


def file_content(request, name=None):
    context = {
        'file_name': name if name else '',
    }
    if name:
        file = path.join(settings.FILES_PATH, name)
        if path.isfile(file):
            context['file_content'] = read_file_to_context(file)
        else:
            context['file_content'] = 'файла не существует'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(request, 'file_content.html', context)
