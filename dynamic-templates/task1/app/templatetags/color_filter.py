from django.template import library


register = library.Library()


@register.filter
def color_filters(value):
    if value:
        if float(value) < 0:
            return 'green'
        elif 1 < float(value) < 2:
            return 'red'
        elif 2 < float(value) < 5:
            return 'indianred'
        elif float(value) > 5:
            return 'darkred'
    return 'white'
