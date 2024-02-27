from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('registre', views.registre, name="registre"),
    path('my-login', views.my_login, name="my-login"),
    path('day-lecture', views.day_lecture, name="day-lecture"),
    path('recherche', views.recherche, name="recherche"),
]
