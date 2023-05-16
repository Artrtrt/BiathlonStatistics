from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .serializers import *
from .models import Season
from russian_names import RussianNames


class SeasonAPIList(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonAPICreate(generics.CreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonAPIUpdate(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonAPIDelete(generics.DestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


# def patch1():
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
#

class ResultAPIList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAPIUpdate(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAPIDelete(generics.DestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAPICreate(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class CompetitionAPIList(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionAPIUpdate(generics.UpdateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionAPIDelete(generics.DestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionAPICreate(generics.CreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
