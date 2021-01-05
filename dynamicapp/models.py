from django.db import models


class StudentDetails(models.Model):
	branches=[('None','None'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE')]
	genders=[('Female','Female'),('Male','Male')]
	languages=[('Telugu','Telugu'),('Hindi','Hindi'),('English','English')]
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	branch = models.CharField(max_length=4, choices=branches, null=True)
	gender = models.CharField(max_length=10, choices=genders, null=True)
	select_lang =models.CharField(max_length=10, choices=languages, null=True)
	email = models.EmailField(max_length=30)
	password=models.CharField(max_length=30)
	age=models.IntegerField(null=True)



class Register1(models.Model):
	gender_ch= [('Male','Male'),('Female','Female')]
	name=models.CharField(max_length=30,null=True)
	mobile_no=models.CharField(max_length=10,null=True)
	age=models.IntegerField()
	gender=models.CharField(max_length=10,choices=gender_ch,null=True)