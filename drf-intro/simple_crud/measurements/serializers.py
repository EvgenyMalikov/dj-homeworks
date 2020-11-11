# TODO: опишите сериализаторы
from rest_framework import serializers

from .models import Project, Measurement


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
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


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, allow_null=True)

    class Meta:
        model = Measurement
        fields = [
            'id',
            'value',
            'project',
            'image'
        ]
