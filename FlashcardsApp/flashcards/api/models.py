from ast import Starred
from django.db import models

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
    name = models.CharField(max_length=50)
    number_cards = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField()
    last_updated = models.DateTimeField()
    color = models.CharField(max_length=10)
    starred = models.BooleanField(default=False)


class Card(models.Model):
    front = models.CharField(max_length=255)
    back = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    starred = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField()
    last_updated = models.DateTimeField()
    state = models.CharField(max_length=50, default='Unrevealed') # Good/Bad/Unrevealed


class Session(models.Model):
    time_spend = models.FloatField(default=0.0) # time in seconds
    number_correct_answers = models.IntegerField(default=0)
    number_studied_cards = models.IntegerField(default=0)
