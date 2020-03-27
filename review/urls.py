from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'homepage'),
    path('review/new/', views.review_create, name = 'review_create'),
    path('courses/', views.courses, name = 'courses'),
    path('profs/', views.profs, name = 'profs'),

]