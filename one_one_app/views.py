from django.shortcuts import render
from django.views import generic
 
 
class HomeView(generic.TemplateView):
    template_name = 'account/home.html'

class WelcomeView(generic.TemplateView):
    template_name = 'welcome.html'
 