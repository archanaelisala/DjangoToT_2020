from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=30)
	rollnum = models.CharField(max_length=20)
	age = models.IntegerField()
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
