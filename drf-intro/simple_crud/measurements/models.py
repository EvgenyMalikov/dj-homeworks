from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True  # Это абстрактный класс и для него не будет создаватся таблица в базе данных


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default='',  upload_to='sensors/%Y/%m/%d/')

    def __str__(self):
        return f'{self.value}'

