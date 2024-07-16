from django.shortcuts import render
from django.views.generic import TemplateView
    
class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'