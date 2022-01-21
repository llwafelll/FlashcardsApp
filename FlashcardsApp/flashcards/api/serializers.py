from rest_framework import serializers
from models import User, Deck, Card, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'age', 'date_created',
                  'date_visited', 'date_updated', 'color', 'starred')


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'name', 'number_cards', 'date_created', 'last_visited',
                  'last_updated', 'color', 'starred')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'front', 'back', 'color', 'starred', 'suspended', 
                  'date_created', 'date_visited', 'last_updated', 'state')


class SessionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'time_spend', 'number_correct_answers',
                  'number_studied_cards')