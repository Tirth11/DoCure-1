from django.urls import include, path
from . import views



urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('home/', views.home, name="home"),


	
    ]