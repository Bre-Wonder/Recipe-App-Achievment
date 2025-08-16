from django.shortcuts import render
# to protect function based view
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm

# Create your views here.


def home(request):
    return render(request, 'sales/home.html')


@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'sales/records.html', context)
