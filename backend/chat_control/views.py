
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from chat_control.models import Message



class MessageAPI(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageAPICreate(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)