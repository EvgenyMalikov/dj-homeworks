from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing_param = request.GET.get('from-landing')
    if from_landing_param == 'test':
        counter_click['test'] += 1
    elif from_landing_param == 'original':
        counter_click['original'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_param = request.GET.get('ab-test-arg')
    if ab_test_param == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    elif ab_test_param == 'original':
        counter_show['original'] += 1
    return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_relation = f'Тестовый лэндинг: количество просмотров{counter_show["test"]},' \
                    f'количество кликов {counter_click["test"]}'
    origin_relation = f'Тестовый лэндинг: количество просмотров{counter_show["original"]},' \
                      f'количество кликов {counter_click["original"]}'
    if counter_show["test"] and counter_click["test"]:
        test_relation = counter_click["test"] / counter_show["test"]
    if counter_click["original"] and counter_show["original"]:
        origin_relation = counter_click["original"] / counter_show["original"]
    return render_to_response('stats.html', context={
        'test_conversion':  test_relation,
        'original_conversion':  origin_relation,
    })
