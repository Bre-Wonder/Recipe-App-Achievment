from django.urls import path
from .views import home

app_name = 'recipeApp'

urlpatterns = [
    path('', home),
]
