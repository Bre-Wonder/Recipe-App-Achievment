from django.shortcuts import render, redirect
# libraries that django has for authentication
from django.contrib.auth import authenticate, login, logout
# form django provides for authentication
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):

    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # checks if form is valid
        if form.is_valid():
            # get request to read username
            username = form.cleaned_data.get('username')
            # get request to reapassword
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('sales:records')

            else:
                error_message = 'ooops... something went wrong'

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect(login)
