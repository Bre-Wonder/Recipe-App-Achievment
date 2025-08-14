from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

# Create your views here.


class RecipeListView(ListView):
    # model that is being communicated with
    model = Recipe
    # template that is being used
    template_name = 'recipeApp/main_recipelist.html'


def home(request):
    return render(request, 'recipeApp/recipe_home.html')
