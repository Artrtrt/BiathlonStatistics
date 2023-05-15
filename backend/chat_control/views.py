
from rest_framework import generics
from rest_framework.generics import CreateAPIView

from .serializers import *

from chat_control.models import Message


class MessageAPI(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageAPICreate(CreateAPIView):
    # def post(self, request):
    #     serializer = MessageSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response({'post': serializer.data})
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
