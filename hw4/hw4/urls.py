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
from blogs.views import create_user, Creation_Post, Update_Post, List_Post, Detail_Post, Delete_Post, My_List_Post
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List_Post.as_view()),
    path('post/myposts/', My_List_Post.as_view()),
    path('register/', create_user),
    path('accounts/login/', LoginView.as_view(template_name='login.html')),
    path('post/new/', Creation_Post.as_view()),
    path('post/<slug>/edit/', Update_Post.as_view(), name = 'post_update'),
    path('post/<slug>/delete/', Delete_Post.as_view(), name = 'post_delete'),
    path('logout/', LogoutView.as_view()),
    path('post/<slug>/',  Detail_Post.as_view(),name = 'post_detail'),
]