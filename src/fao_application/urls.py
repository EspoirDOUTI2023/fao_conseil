from django.urls import path
from .views import accueil, analyse

urlpatterns = [
    path('', accueil, name='accueil'),
    path('analyse/', analyse, name='analyse')
]

