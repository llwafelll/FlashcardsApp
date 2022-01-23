from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (UserSerializer, CardGetSerializer,
                          DeckGetSerializer, SessionSerilizer,
                          DeckPostSerializer, DeckPutSerializer,
                          CardGetSerializer)
from .models import User, Card, Deck, Session

# Create your views here.
def index(request):
    return HttpResponse("This is API.")


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DecksView(APIView):
    def get(self, request, format=None):
        decks = Deck.objects.all()
        if len(decks) > 0:
            data = DeckGetSerializer(decks, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "The deck is empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = DeckPostSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            color = serializer.data.get('color')
            starred = serializer.data.get('starred')
             
            deck = Deck(name=name, color=color, starred=starred)
            deck.save()
            
            return Response(DeckGetSerializer(deck).data, status=status.HTTP_201_CREATED)


class DeckView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Deck.objects.filter(name=kwargs['name'])
        if queryset.count() == 1:
            requested_deck = queryset[0]
            data = DeckGetSerializer(requested_deck).data
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, format=None, *args, **kwargs):
        queryset = Deck.objects.filter(name=kwargs['name'])
        serializer = DeckPutSerializer(data=request.data)

        if (queryset.count() == 1) and serializer.is_valid():
            requested_deck = queryset[0]
            requested_deck.color = serializer.data.get('color')
            requested_deck.starred = serializer.data.get('starred')

            requested_deck.save()

            return Response(DeckGetSerializer(requested_deck).data,
                            status=status.HTTP_202_ACCEPTED)

        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, format=None, *args, **kwargs):
        deleted_object = Deck.objects.filter(name=kwargs['name']).delete()
        if deleted_object:
            return Response(deleted_object[1], status=status.HTTP_200_OK)
        
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class CardsView(APIView):
    def get(self, request, format=None):
        queryset = Card.objects.all()
        if queryset.count() > 0:
            data = CardGetSerializer(queryset, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "There is no single card in any deck"},
                        status=status.HTTP_400_BAD_REQUEST)


class CardView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Card.objects.filter(id=kwargs['id'])

        if queryset.count() == 1:
            requested_card = queryset[0]
            data = CardGetSerializer(requested_card).data
            
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "This card does not exist"},
                        status=status.HTTP_400_BAD_REQUEST)


class DeckCardView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        deck_queryset = Deck.objects.filter(id=kwargs['name'])
        card_queryset = Card.objects.filter(id=kwargs['id'])

        if deck_queryset.count() == 1 and card_queryset.count() == 1:
            requested_card = card_queryset[0]
            data = CardGetSerializer(requested_card).data
            
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "Requested card does not exist in given deck"},
                        status=status.HTTP_400_BAD_REQUEST)


class SessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerilizer