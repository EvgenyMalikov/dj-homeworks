from django import template
from datetime import timedelta, datetime

register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    now_ = datetime.now()
    post_date = datetime.fromtimestamp(value)
    if now_ < post_date:
        return 'так не бывает'
    delta = now_ - post_date
    if delta < timedelta(minutes=10):
        return 'Только что'
    if delta > timedelta(days=1):
        return datetime.strftime(post_date, '%Y-%m-%d')
    if delta < timedelta(days=1):
        return f'{delta.seconds // 3600 } часов назад'


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value=0):
    if value < -5:
        return 'Все плохо'
    if value -5 <= value <= 5:
        return 'Нейтрально'
    if value > 5:
        return 'Хорошо'
    return value


@register.filter
def format_num_comments(value) -> str:
    # Ваш код
    if value == 0:
        return 'Оставьте комментарий'
    if 0 < value < 50:
        return f'{value}'
    else:
        return f'50+'


@register.filter
def format_selftext(value='', count=0) -> str:
    if not value:
        return value
    value = value.split(' ')
    return '...'.join((' '.join(value[:count]), ' '.join(value[-count::1])))
