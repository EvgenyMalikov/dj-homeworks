from django.views.generic import ListView

from .models import Article


class ArticlesList(ListView):
    queryset = Article.objects.prefetch_related('scopes').all().order_by('-published_at')
    template_name = 'articles/news.html'
