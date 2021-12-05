"""hw4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs.views import create_user, Creation_Post, Update_Post, List_Post, Detail_Post, Delete_Post,My_List_Post,My_List_View
import django.contrib.auth.views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List_Post.as_view()),
    path('post/myposts/', My_List_View),
    path('register/', create_user),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('post/new', Creation_Post.as_view()),
    path('post/<slug:slug>/edit', Update_Post.as_view(), name = 'post_update'),
    path('post/<slug:slug>/delete', Delete_Post.as_view(), name = 'post_delete'),
    path('logout/', auth_views.LogoutView.as_view()),
    path('post/<slug:slug>/',  Detail_Post.as_view(),name = 'post_detail'),
]