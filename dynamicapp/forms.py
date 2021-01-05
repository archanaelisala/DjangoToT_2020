from django import forms
from django.forms import ModelForm
from .models import Register1

class RegisterForm(forms.ModelForm):
	class Meta:
		model=Register1
		fields='__all__'
		#fields=['name','age']

		widgets={
		"name":forms.TextInput(attrs={'placeholder':'enter name','class':'form-control'}),
		'mobile_no':forms.TextInput(attrs={'placeholder':'enter mobile_no','class':'form-control'}),
		'age':forms.NumberInput(attrs={'required':False,'placeholder':'enter age','class':'form-control'}),
		'gender':forms.RadioSelect(attrs={'class':'radio-inline form-group'})
		}



gender_ch= [('Male','Male'),('Female','Female')]
langs=[('English','English'),('Telugu','Telugu'),('Hindi','Hindi')]
branches=[('None','None'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('Mech','Mech'),('Civil','Civil'),('IT','IT')]
class Emp(forms.Form):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Firstname','class':'form-control my-1'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter lastname','class':'form-control my-1'}))
	branch=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=branches)
	age=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control my-1'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-1','placeholder':'Enter Email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-1','placeholder':'Enter Password'}))
	gender=forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline form-group'}),choices=gender_ch)
	#dropdown
	#select_gender=forms.ChoiceField(widget=forms.Select,choices=gender_ch)
	#select_lang=forms.ChoiceField(widget=forms.Select,choices=langs)

	select_lang=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=langs)	





