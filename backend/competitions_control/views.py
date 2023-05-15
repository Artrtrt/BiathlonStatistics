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


class SeasonAPIUpdateDestroy(mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


class ResultAPIUpdateDestroy(mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ResultAPICreate(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class CompetitionAPIList(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionAPIUpdateDestroy(mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  GenericAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompetitionAPICreate(generics.CreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
