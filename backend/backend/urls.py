
from django.urls import path

from chat_control.views import MessageAPI, MessageAPICreate
from competitions_control.views import *
from .yasg import urlpatterns as doc_urls

from users_control.views import RegistrUserView, TokenCreateViewApi

urlpatterns = [
    path("seasons/", SeasonAPIList.as_view()),
    path("results/", ResultAPIList.as_view()),
    path("competitions/", CompetitionAPIList.as_view()),
    path("add_season/", SeasonAPICreate.as_view()),
    path("add_competition/", CompetitionAPICreate.as_view()),
    path('update_season/<int:pk>/', SeasonAPIUpdate.as_view()),
    path('update_competition/<int:pk>/', CompetitionAPIUpdate.as_view()),
    path('delete_season/<int:pk>/', SeasonAPIDelete.as_view()),
    path('delete_result/<int:pk>/', ResultAPIDelete.as_view()),
    path('delete_competition/<int:pk>/', CompetitionAPIDelete.as_view()),
    path('registration/', RegistrUserView.as_view()),
    path('login/', TokenCreateViewApi.as_view()),
    path('all_chat/', MessageAPI.as_view()),
    path('add_message/', MessageAPICreate.as_view()),
    path('delete_category/', CategoryAPIDelete.as_view()),
    path('add_category/', CategoryAPICreate.as_view()),

]
urlpatterns += doc_urls