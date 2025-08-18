from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
# import form from forms.py
from .forms import IngredientSearchForm


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

    # packs up dtat to be sent to template in the form of a dictionary
    context = {
        'form': form,
    }

    return render(request, 'recipeApp/ingredient_search.html', context)
