from rest_framework import serializers
from russian_names import RussianNames

from competitions_control.models import *


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"


class CategoryDeleteSerializer(serializers.Serializer):
    competititon_id = serializers.CharField(max_length=128, required=True)
    category = serializers.CharField(max_length=128, required=True)

    class Meta:
        fields = ('competititon_id', 'category')

