from django.urls import path
from phone import views

urlpatterns =[
    path('', views.index, name='index')
]
