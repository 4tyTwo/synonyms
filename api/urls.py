from django.urls import path

from . import views

urlpatterns = [
    path('synonyms/<str:word>', views.most_similar, name='Synonyms'),
]