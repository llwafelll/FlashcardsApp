from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (UserSerializer, CardGetSerializer,
                          DeckGetSerializer, SessionSerilizer,
                          DeckPostSerializer, DeckPutSerializer,
                          CardGetSerializer, CardPostSerializer,
                          CardPatchSerializer)
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
        deck_queryset = Deck.objects.filter(name=kwargs['name'])
        card_queryset = Card.objects.filter(id=kwargs['id'])

        if deck_queryset.count() == 1 and card_queryset.count() == 1:
            requested_card = card_queryset[0]
            data = CardGetSerializer(requested_card).data
            
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "Requested card does not exist in given deck"},
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None, *args, **kwargs):
        try:
            requested_deck = Deck.objects.get(name=kwargs['name'])
        except ObjectDoesNotExist:
            return Response({"No data": "Deck not found."},
                            status=status.HTTP_404_NOT_FOUND)
            
        try:
            requested_card = requested_deck.cards.get(id=kwargs['id'])
        except ObjectDoesNotExist:
            return Response({"No data": "No card in specified deck."},
                            status=status.HTTP_404_NOT_FOUND)
        
        serializer = CardPatchSerializer(requested_card, data=request.data,
                                         partial=True)

        if serializer.is_valid():
            serializer.save()

            # return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        try:
            requested_deck = Deck.objects.get(name=kwargs['name'])
        except ObjectDoesNotExist:
            return Response({"No data": "Deck not found."},
                            status=status.HTTP_404_NOT_FOUND)
            
        try:
            requested_card = requested_deck.cards.get(id=kwargs['id'])
        except ObjectDoesNotExist:
            return Response({"No data": "No card in specified deck."},
                            status=status.HTTP_404_NOT_FOUND)
        
        requested_card.delete()
        return Response({"deleted": "Card deleted."},
                        status=status.HTTP_200_OK)
        
        
class DeckCardsView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        deck_queryset = Deck.objects.filter(name=kwargs['name'])

        if deck_queryset.count() == 1:
            requested_deck = deck_queryset[0]
            card_queryset = requested_deck.cards.all()
            data = CardGetSerializer(card_queryset, many=True).data

            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"No data": "Requested deck does not exist"})
        
    def post(self, request, format=None, *args, **kwargs):
        serializer = CardPostSerializer(data=request.data)
        deck_queryset = Deck.objects.filter(name=kwargs['name'])
        if serializer.is_valid() and deck_queryset.count() == 1:
            requested_deck = deck_queryset[0]

            front = serializer.data.get('front')
            back = serializer.data.get('back')
            color = serializer.data.get('color')
            starred = serializer.data.get('starred')
            suspended = serializer.data.get('suspended')
            
            card = Card(front=front, back=back, color=color, starred=starred,
                        suspended=suspended, deck=requested_deck)
            card.save()

            return Response(CardGetSerializer(card).data, status=status.HTTP_200_OK)
        
        return Response({"Object not created": "Createtion aborded."})
    
    def delete(self, request, format=None, *args, **kwargs):
        deck_queryset = Deck.objects.filter(name=kwargs['name'])
        if deck_queryset.count() == 1:
            requested_deck = deck_queryset[0]
            deleted_cards = requested_deck.cards.all().delete()

            return Response(deleted_cards, status=status.HTTP_200_OK)
        
        return Response({"No data": "There is no single card in any deck"},
                        status=status.HTTP_400_BAD_REQUEST)
            

class SessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerilizer