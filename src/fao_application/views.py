from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'fao/accueil.html')

def analyse(request):
    return render(request, 'fao/analyse.html')


