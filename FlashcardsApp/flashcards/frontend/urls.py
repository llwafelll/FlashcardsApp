from django.urls import path
from .views import index


urlpatterns = [
    path('', index),
    path('deck/<str:name>', index),
    path('deck/<str:name>/card/<str:id>', index),
    path('deck/<str:name>/card', index),
    path('deck', index),
]