"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from djtot import views
from secondapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('about/',views.about),
    path('string_value/<str:name>/',views.String),
    path('table/<int:num>',views.table),
    path('twoparameters/<str:name1>/<int:age>',views.twoVar),
    path('cssex/',views.cssexample),
    path('login',views.Login),
    path('register',views.Register),
    path('javascript',views.Javascript_Ex),
    path('bootstrapex',views.LoginRegister),
    path('bootstrapex2',views.boost),

    ## SecondAPP

    path('newlogin',v.newlogin),
    path('newregister',v.regi),

    #third app
    path('crud/',include('CRUD.urls')),

    #4th app
    path('formapp/',include('dynamicapp.urls'))




]
