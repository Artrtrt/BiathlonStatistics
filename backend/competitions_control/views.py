from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import Season


class SeasonAPI(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


# class SeasonAPIUpdate(generics.UpdateAPIView):
#     queryset = Season.objects.all()
#     serializer_class = SeasonSerializer


class ResultAPI(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


# class CompetitionAPIUpdate(generics.UpdateAPIView):
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializer


class CompetitionAPI(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


# class CompetitionAPIUpdate(generics.UpdateAPIView):
#     queryset = Competition.objects.all()
#     serializer_class = CompetitionSerializer
