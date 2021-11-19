from django.shortcuts import render, redirect
# from django import forms
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth import password_validation



# Create your views here.


# class RegisterForm(UserCreationForm):

# 	password1 = forms.CharField(
#     label="пароль 1",
#     widget=forms.PasswordInput,
#     help_text=password_validation.password_validators_help_text_html(""),
#     #help_text = 'jghfjgfjhg'
# )
# 	password2 = forms.CharField(
#     label="пароль 2",
#     help_text=password_validation.password_validators_help_text_html(),
#    # help_text = 'jghfjgfjhg'
# )

			


def create_user(request):
	#form = RegisterForm(request.POST or None)
	form = UserCreationForm(request.POST or None)
	if form.is_bound and form.is_valid():
	 	user = form.save()
	 	return redirect('/accounts/login/')
	return render(request, 'register.html', {'form':form})

def index(request):
	return render(request, 'index.html')
