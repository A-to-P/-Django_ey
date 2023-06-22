from django.shortcuts import render
from .forms import UserLoginForm, UserSignUpForm

def signin(request):
    return render(request, 'signin.html')


def signup(request):
    form = UserSignUpForm
    return render(request, 'signup.html', {'form' : form})