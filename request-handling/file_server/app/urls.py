from django.urls import path, register_converter
from . import views
from .converters import  DateConverter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
register_converter(DateConverter, 'dt')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', views.file_list, name='file_list'),
    path('<dt:date>/', views.file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('files/<name>', views.file_content, name='file_content'),
]
