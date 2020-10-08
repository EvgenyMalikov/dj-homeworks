from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    image = models.CharField(max_length=200)
    release_date = models.DateField(blank=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


