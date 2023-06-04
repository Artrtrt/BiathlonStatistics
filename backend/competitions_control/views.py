from requests import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from competitions_control.serializers import *
from swagger_docs import *


class SeasonAPIList(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    @season_get_all
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SeasonAPICreate(generics.CreateAPIView):
    @season_create
    def post(self, request, **kwargs):
        serializer = SeasonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'id': serializer.data.get('id')})


class SeasonAPIUpdate(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)
    @season_put
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @season_patch
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SeasonAPIDelete(generics.DestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminUser,)

    @season_delete
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ResultAPIList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    @result_get_all
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResultAPIUpdate(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (IsAdminUser,)
    @result_put
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @result_patch
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CategoryAPIDelete(APIView):
    permission_classes = (IsAdminUser,)
    @category_delete
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
    permission_classes = (IsAdminUser,)

    @category_create
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

    @result_delete
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompetitionAPIList(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    @competition_get_all
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CompetitionAPIUpdate(generics.UpdateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAdminUser,)
    @competition_put
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @competition_patch
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CompetitionAPIDelete(generics.DestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAdminUser,)

    @competition_delete
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompetitionAPICreate(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    @competition_create
    def post(self, request, **kwargs):
        serializer = CompetitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'id': serializer.data.get('id')})
