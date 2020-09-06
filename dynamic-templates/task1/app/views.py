from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(settings.INFLATION_FILE) as csv_inflation:
        list_inflation = list(csv.reader(csv_inflation, delimiter=';'))
    context = {
        'inflation_head': list_inflation.pop(0),
        'inflation': list_inflation
    }

    return render(request, template_name,
                  context)