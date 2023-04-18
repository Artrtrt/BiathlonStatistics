from django.http import HttpResponse
from django.shortcuts import render
from pymongo.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from russian_names import RussianNames
from .serializers import *
from .models import Season
from russian_names import RussianNames


class SeasonAPI(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


# class SeasonAPIUpdate(generics.UpdateAPIView):
#     queryset = Season.objects.all()
#     serializer_class = SeasonSerializer


class ResultAPI(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # def bd(self):
    #     for n in range(1078):
    #         c = Result.objects.get(pk=n)
    #         c.sportsman = RussianNames().get_person()


# class CompetitionAPIUpdate(generics.UpdateAPIView):
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializer


class CompetitionAPI(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    # class CompetitionAPIUpdate(generics.UpdateAPIView):
    #     queryset = Competition.objects.all()
    #     serializer_class = CompetitionSerializer

# Заполняет таблицу имен
# def patch():
#     for n in range(1, 1061):
#         c = Result.objects.get(pk=n)
#         b = "Мужчины"
#         v = "Женщины"
#         if b in Result.objects.get(pk=n).category:
#             c.sportsman = RussianNames(gender=1).get_person()
#             c.save(update_fields=["sportsman"])
#         else:
#             if v in Result.objects.get(pk=n).category:
#                 c.sportsman = RussianNames(gender=0).get_person()
#                 c.save(update_fields=["sportsman"])
#             else:
#                 c.sportsman = RussianNames().get_person()
#                 c.save(update_fields=["sportsman"])
