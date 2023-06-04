from djoser.views import TokenCreateView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from djoser.views import TokenCreateView
from rest_framework import status
from swagger_docs import *
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegistrSerializer

from djoser import utils
from djoser.conf import settings


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserRegistrSerializer

    permission_classes = [AllowAny]

    @user_registration
    def post(self, request, *args, **kwargs):

        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:

            data = serializer.errors
            return Response(data)


class TokenCreateViewApi(TokenCreateView):
    serializer_class = settings.SERIALIZERS.token_create
    permission_classes = settings.PERMISSIONS.token_create

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token
        return Response(
            data=(token_serializer_class(token).data, ({"first_name": serializer.user.first_name}),
                  ({"last_name": serializer.user.last_name}), ({"is_superuser": serializer.user.is_superuser})),
            status=status.HTTP_200_OK,

        )

    @user_login
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
