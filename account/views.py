from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LogInForm

# Create your views here.

def signuppage(request):
    forms = UserCreationForm()
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')

    context = {
        'form': forms
    }
    return render(request, 'account/register.html', context)



def dashdoard(request):
    return render(request, 'dashdoard/dashdoard.html')



def loginpage(request):
    forms = LogInForm(request.POST or None)
    if forms.is_valid():
        username = forms.cleaned_data['username']
        password = forms.cleaned_data['password']

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        context = {
            'forms': forms,
            'error': 'Something is wrong..'
        }
        return render(request, 'account/login.html', context)






    context = {
        'forms': forms,

    }
    return render(request, 'account/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')