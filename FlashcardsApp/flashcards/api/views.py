from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import generics

from .serializers import (UserSerializer, CardSerializer,
                          DeckSerializer, SessionSerilizer)
from .models import User, Card, Deck, Session

# Create your views here.
def index(request):
    return HttpRequest("This is API.")


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeckView(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class CardView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class SessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerilizer