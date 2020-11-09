from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count > 1:
            raise ValidationError('Может быть только один главный тэг')
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Tag.article.through
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ScopeInLine
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class CategoryAmin(admin.ModelAdmin):
    pass
