from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.views import LogoutView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class My_List_Post(ListView):
	model = Post
	template_name = 'my_post.html'

	def get_queryset(self):
		user = self.request.user
		if user:
			return self.model.objects.filter(created_by=user)
		return self.model.objects.all()

def create_user(request):
	form = UserCreationForm(request.POST or None)
	if form.is_bound and form.is_valid():
	 	user = form.save()
	 	return redirect('/accounts/login/')
	return render(request, 'register.html', {'form':form})


class Creation_Post( LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','text']
	template_name = 'create.html'


	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(Creation_Post, self).form_valid(form)


class Update_Post(LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title','text']
	template_name = 'update.html'


class List_Post(ListView):
    model = Post
    template_name = 'index.html'


class Detail_Post(DetailView):
	model = Post
	template_name = 'detail.html'


class Delete_Post(LoginRequiredMixin,DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = '/'