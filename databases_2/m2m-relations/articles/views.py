from django.views.generic import ListView

from .models import Article


class ArticlesList(ListView):
    model = Article
    queryset = model.objects.prefetch_related('scopes')
    ordering = '-published_at'
    template_name = 'articles/news.html'
