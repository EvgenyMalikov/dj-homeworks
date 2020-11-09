from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from .bus_stations import read_bus_station
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    paginator = Paginator(read_bus_station(settings.BUS_STATION_CSV), 13)
    current_page = int(request.GET.get('page', 1))
    bus_stations_ = paginator.get_page(current_page)
    next_page_url, prev_page_url = None, None
    if bus_stations_.has_next():
        next_page_url = '?'.join((reverse('bus_stations'), urlencode({'page': bus_stations_.next_page_number()})))
    if bus_stations_.has_previous():
        prev_page_url = '?'.join((reverse('bus_stations'), urlencode({'page': bus_stations_.previous_page_number()})))
    return render(request, 'index.html' , context={
        'bus_stations': bus_stations_,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url':  next_page_url,
    })

