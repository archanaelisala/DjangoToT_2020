from django.urls import path
from CRUD import views

urlpatterns = [
		path('sample/',views.hello)
]