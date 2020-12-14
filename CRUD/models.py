from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=30)
	rollnum = models.CharField(max_length=20)
	age = models.IntegerField()
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	# address = models.TextField(null=True)


	def __str__(self):
		return self.name+" "+self.email



class Emp(models.Model):
	Ename = models.CharField(max_length=30)
	Eid = models.CharField(max_length=20)
	Esal = models.IntegerField()
	mobile = models.CharField(max_length=10)
	Email = models.CharField(max_length=30)
	Eaddress = models.TextField(max_length=30)
	#Eresume = models.FileField(upload_to = 'path/')
	#Eimg = models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100)


	def __str__(self):
		return self.Ename

