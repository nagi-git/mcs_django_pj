from django.urls import path
from one_one_app import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]