from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from swagger_docs import *
from chat_control.models import Message


class MessageAPI(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    @message_get_all
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MessageAPICreate(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    @message_create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
