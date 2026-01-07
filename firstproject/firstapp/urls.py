from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_word),
    path('class', views.Helloindia.as_view()),
    path('reservation',views.home),
]