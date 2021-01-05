from django.urls import path
from dynamicapp import views

urlpatterns = [
	path('dynamic/',views.dynamic,name='dynamic'),
	#path('show/',views.show,name='show'),
	path('registerform/',views.registerform,name='registerform'),
	path('display1/',views.display,name='display'),
	path('homepage/',views.homepage,name='homepage'),
	path('edit/',views.Edit,name='Edit')
	#path('')

	]