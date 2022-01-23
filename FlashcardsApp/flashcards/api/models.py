from ast import Starred
from re import T
from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    email = models.EmailField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    number_decks = models.IntegerField()
    number_cards = models.IntegerField()


class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False,
                            primary_key=True, default="[New deck]")
    number_cards = models.IntegerField(default=0, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=10, null=True)
    starred = models.BooleanField(default=False)

    # user = models.ForeignKey(User, on_delete=models.CASCA, null=Trueue)


class Card(models.Model):
    front = models.CharField(max_length=255)
    back = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    starred = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=50, default='Unrevealed') # Good/Bad/Unrevealed

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')


class Session(models.Model):
    time_spend = models.FloatField(default=0.0) # time in seconds
    number_correct_answers = models.IntegerField(default=0)
    number_studied_cards = models.IntegerField(default=0)
