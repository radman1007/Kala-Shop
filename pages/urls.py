from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.AboutUsPageView.as_view(), name='aboutus'),
]
