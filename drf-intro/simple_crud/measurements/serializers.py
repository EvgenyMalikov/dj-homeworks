# TODO: опишите сериализаторы
from rest_framework import serializers

from .models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Project
        fields = [
           'id',
           'name',
           'latitude',
           'longitude',
           'created_at',
           'updated_at'
        ]


class MeasurementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, default='')

    class Meta:
        model = Measurement
        fields = [
            'id',
            'value',
            'project',
            'image'
        ]
