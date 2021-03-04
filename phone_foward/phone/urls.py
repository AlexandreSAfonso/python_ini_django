from django.urls import path
import phone.views as views


urlpatterns =[
    path('', views.index, name='index'),
    path('registered', views.registered_func, name='registered_func'), 
]
