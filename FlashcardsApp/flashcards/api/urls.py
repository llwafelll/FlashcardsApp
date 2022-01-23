from django.urls import path
from django.http import HttpResponse
from .views import (index, UserView, DecksView, CardsView, DeckView,
                    DeckCardsView, DeckCardView)


urlpatterns = [
    path('', index),
    path('deck/', DecksView.as_view()),
    path('deck/<str:name>', DeckView.as_view()),
    path('card/', CardsView.as_view()),
    path('deck/<str:name>/card', DeckCardsView.as_view()),
    path('deck/<str:name>/card/<str:id>', DeckCardView.as_view()),
]
