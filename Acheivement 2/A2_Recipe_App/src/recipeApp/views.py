from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
# import form from forms.py
from .forms import IngredientSearchForm, ChartForm
# installed pandas, now importing it
import pandas as pd
# allows queries to use the OR operator
from django.db.models import Q


# Create your views here.


class RecipeListView(LoginRequiredMixin, ListView):
    # model that is being communicated with
    model = Recipe
    # template that is being used
    template_name = 'recipeApp/main_recipelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IngredientSearchForm()
        return context


class RecipeDetailView(LoginRequiredMixin, DetailView):
  # model that is being communicated with
    model = Recipe
    # template that is being used
    template_name = 'recipeApp/recipe_details.html'


def home(request):
    return render(request, 'recipeApp/recipe_home.html')

 # function that send in form for the user


def IngredientSearch(request):
  # creates an instance of the form
    form = IngredientSearchForm(request.POST or None)
    recipeApp_df = None

    # checks to see if search button is clicked
    if request.method == 'POST':
        # reads recipe_title
        recipe_title = request.POST.get('recipe_title')
        # reads chart_type - going to comment this out for now since I'm not sure I will be using it here
        # chart_type = request.POST.get('chart_type')
        print(recipe_title)
        # print(chart_type)

        # filter for user to be able to find recipe name and ingredients in the Recipe object
        qs = Recipe.objects.filter(Q(name__icontains=recipe_title) | Q(
            ingredients__icontains=recipe_title))
        print(qs)

    # packs up dtat to be sent to template in the form of a dictionary
    context = {
        'form': form,
        'qs': qs
    }

    return render(request, 'recipeApp/ingredient_search.html', context)


def DifficultyChart(request):
    form = ChartForm(request.POST or None)

    context = {
        'form': form,
    }
    return render(request, 'recipeApp/charts.html', context)
