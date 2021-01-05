from django.urls import path
from CRUD import views

urlpatterns = [
		path('sample/',views.hello),
		path('addstudent/',views.AddStudent,name='AddStudent'),  #insertion

		path('read/',views.read,name='read'),  #retrieving
		path('edit/<int:id>',views.edit,name="edit"),
		path('delete/<int:id>',views.Delete,name='Delete'),



		#radi,checkbox updation task
		path('addnewrecord/',views.AddNew,name='AddNew'),
		path('displaydata/',views.Display,name='Display'),
		path('update/<int:id>',views.update,name='update'),
		path('delete/<int:id>',views.deleteNew,name='deleteNew')



]