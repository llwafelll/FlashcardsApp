from django.urls import path
from .views import index, UserView


urlpatterns = [
    path('', index),
    path('user/', UserView.as_view()),
]
