"""Auth URL Configuration

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
from django.urls import path,include
from home import views

urlpatterns = [
        path('admin/', admin.site.urls),
    path('', views.homebefore, name="homebefore"),
    path('home/', views.home, name="home"),
    path('homebefore/', views.homebefore, name="homebefore"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	# path('sign/', views.sign, name="sign"),
	path('logout/',views.logout_view,name='logout'),
    path('about/',views.about,name='about'),
      path('report/',views.report,name='report'),
 	path('FILE/',views.FILE,name='FILE'),
  path('dashboard/',views.dashboard,name='dashboard'),
  
    
]
