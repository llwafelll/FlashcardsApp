from rest_framework import serializers
from .models import User, Deck, Card, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'age', 'email',
                  'date_added', 'number_decks', 'number_cards')


class DeckGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'number_cards', 'date_created', 'last_visited',
                  'last_updated', 'color', 'starred')

class DeckPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'color', 'starred')

class DeckPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('color', 'starred')


class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'front', 'back', 'color', 'starred', 'suspended', 
                  'date_created', 'last_visited', 'last_updated', 'state')


class CardPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('front', 'back', 'color', 'starred', 'suspended')


class CardPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('front', 'back', 'color', 'starred', 'suspended')

class SessionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'time_spend', 'number_correct_answers',
                  'number_studied_cards')