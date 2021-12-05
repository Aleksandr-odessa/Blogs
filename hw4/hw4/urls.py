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
from blogs.views import create_user, CreationPost, UpdatePost,BlogListView,PostDetailView
import django.contrib.auth.views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogListView.as_view()),
    path('register/', create_user),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('post/', CreationPost.as_view()),
    path('<int:pk>/update/', UpdatePost.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('post/<slug:slug>/', PostDetailView.as_view()),
]