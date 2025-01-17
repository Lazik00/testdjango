from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class homePage(TemplateView):
    template_name = 'homepage.html'

class signup(TemplateView):
    template_name = 'signup.html'
class signin(TemplateView):
    template_name = 'signin.html'