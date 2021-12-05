from django.shortcuts import render, redirect
# from django import forms
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView, ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import password_validation


class CreationPost( LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','text']
	template_name = 'login.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(CreationPost, self).form_valid(form)


class UpdatePost(UpdateView):
	model = Post
	fields = ['title','text', 'created_by']
	template_name = 'update.html'

class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

def create_user(request):
	#form = RegisterForm(request.POST or None)
	form = UserCreationForm(request.POST or None)
	if form.is_bound and form.is_valid():
	 	user = form.save()
	 	return redirect('/post/')
	return render(request, 'register.html', {'form':form})

def logout_view(request):
	if request.user.is_authenticated:
		logout()