from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


from django.contrib.auth import views
from django.conf.urls import url
from . import views


urlpatterns = [
    path('home/', login_required(views.HomeView.as_view()), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='register'),
]