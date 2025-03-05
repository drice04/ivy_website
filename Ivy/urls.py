from django.urls import path
from Ivy import views

app_name = 'Ivy'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
]