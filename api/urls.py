from django.urls import path

from . import views

urlpatterns = [
    path('synonyms/', views.most_similar, name='Synonyms'),
]