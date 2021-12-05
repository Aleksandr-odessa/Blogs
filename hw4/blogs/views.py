from django.shortcuts import render, redirect
# from django import forms
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


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
		return super(CreationPost, self).form_valid(form)


class Update_Post(UpdateView):
	model = Post
	fields = ['title','text']
	template_name = 'update.html'


class List_Post(ListView):
    model = Post
    template_name = 'index.html'

class My_List_Post(ListView):
	model = Post
	template_name = 'my_Posts.html'


def My_List_View(request):
	context = {'title': Post.objects.filter(created_by=request.user)}
	print(context[Post])
	return render(request, 'my_Posts.html', context)


class Detail_Post(DetailView):
	model = Post
	template_name = 'detail.html'

class Delete_Post(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = '/'
	#success_url = reverse_lazy('post_detail')


def logout_view(request):
	if request.user.is_authenticated:
		logout()

