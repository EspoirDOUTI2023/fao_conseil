from django.urls import path
from .views import accueil, analyse, echange

urlpatterns = [
    path('', accueil, name='accueil'),
    path('analyse/', analyse, name='analyse'),
    path('echange/', echange, name='echange')
]

