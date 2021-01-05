from django.shortcuts import render,redirect
from django.http import HttpResponse

from dynamicapp.forms import Emp
from dynamicapp.forms import RegisterForm
from dynamicapp.models import StudentDetails
from dynamicapp.models import Register1
# Create your views here.

def registerform(request):
	if request.method=='POST':
		# data=request.POST
		# print(data)
		# return HttpResponse("Done")
		f=RegisterForm(request.POST)
		if f.is_valid():
			f.save()
		#return HttpResponse("successfully inserted")
		# f.save()
		#return HttpResponse("successfully inserted")
		return redirect('/formapp/homepage')

	f=RegisterForm()
	return render(request,'dynamicapp/registerForm.html',{'form':f})


def display(request):
	data1=Register1.objects.all()
	#print(data)
	#return HttpResponse("welcome")

	return render(request,'dynamicapp/display1.html',{'data':data1})



def homepage(request):
	#return redirect('registerform')
	return render(request,'dynamicapp/navbar.html')






def dynamic(request):
	t=Emp()
	if request.method=="POST":
		fn=request.POST['firstname']
		ln=request.POST['lastname']
		br=request.POST['branch']
		age=request.POST['age']
		email=request.POST['email']
		pwd=request.POST['password']
		gen=request.POST['gender']
		lan=request.POST['select_lang']
		return render(request,'dynamicapp/display.html',{'fn':fn,'ln':ln,'br':br,'age':age,'email':email,'pwd':pwd,'gen':gen,'lan':lan})
	return render(request,'dynamicapp/dynamic.html',{'form':t})



def Edit(request,id):
	d = Register1.objects.get(id=id)
	if request.method == "POST":
		form = RegisterForm(request.POST,instance)
		if form.is_valid():
			form.save()
			return HttpResponse("successfully completed")
		form = RegisterForm()
		return render(request,'dynamicapp/update.html',{"d":d})
