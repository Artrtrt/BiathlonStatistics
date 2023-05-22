from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.views import APIView

from .serializers import *
from .models import Season


class SeasonAPIList(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer



class SeasonAPICreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, **kwargs):
        serializer = SeasonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'id': serializer.data.get('id')})


class SeasonAPIUpdate(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)


class SeasonAPIDelete(generics.DestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)


class ResultAPIList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAPIUpdate(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (IsAdminUser,)


class CategoryAPIDelete(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        competition_id = request.data.get('competition_id')
        category = request.data.get('category')

        if competition_id is not None and category is not None:
            results_to_delete = Result.objects.filter(
                competition_id=competition_id, category=category
            )
            results_to_delete.delete()
            return Response({'Удалилось'})
        else:
            return Response({'Потренеруйся и попробуй еще раз'})


class CategoryAPICreate(APIView):
    # permission_classes = (IsAdminUser,)

    def post(self, request):
        data = request.data

        list_temp: list = []

        for value in data['array']:
            value['competition'] = data['competition']
            list_temp.append(value)
        print(list_temp)

        serializer = ResultSerializer(data=list_temp, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response({'data': data})


class ResultAPIDelete(generics.DestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (IsAdminUser,)


class ResultAPICreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, **kwargs):
        serializer = ResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'id': serializer.data.get('id')})


class CompetitionAPIList(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionAPIUpdate(generics.UpdateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAdminUser,)


class CompetitionAPIDelete(generics.DestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAdminUser,)


class CompetitionAPICreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, **kwargs):
        serializer = CompetitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'id': serializer.data.get('id')})
