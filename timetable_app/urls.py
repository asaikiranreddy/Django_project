# timetable_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_timetable/', views.generate_timetable, name='generate_timetable'),
    path('timetable_generator/', views.timetable_generator, name='timetable_generator'),
    path('register/', views.user_registration, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
