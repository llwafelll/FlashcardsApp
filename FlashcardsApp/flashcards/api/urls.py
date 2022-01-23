from django.urls import path
from django.http import HttpResponse
from .views import index, UserView, DecksView, CardsView, DeckView


urlpatterns = [
    path('', index),
    path('deck/', DecksView.as_view()),
    path('deck/<str:name>', DeckView.as_view()),
    path('card/', CardsView.as_view()),
]
