from django.urls import path
from .views import accueil, analyse, echange, upload_file, chat, analyse_action

urlpatterns = [
    path('', accueil, name='accueil'),
    path('analyse/', analyse, name='analyse'),
    path('echange/', echange, name='echange'),
    path('upload-file/', upload_file, name='upload_file'),
    path('chat/', chat, name='chat'),
    path('analyse_action/', analyse_action, name='analyse_action')
]

