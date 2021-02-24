from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

def Atlus(request):
    return render(request, 'static/Atlus.html')

def Boomerang(request):
    return render(request, 'static/Boomerang.html')

def Cataract(request):
    return render(request, 'static/Cataract.html')

def Diclonius(request):
    return render(request, 'static/Diclonius.html')

