from django.shortcuts import render,redirect
from django.http import HttpResponse
from CRUD.models import Student,StudentNew

# Create your views here.
def hello(request):
	return HttpResponse("Welcome to ThirdApp Crud")




def AddStudent(request):
	if request.method == "POST":
		sname = request.POST.get('Studentname')
		srollnum = request.POST.get('rollnum')
		sage = request.POST.get('age')
		sphone = request.POST.get('phone')
		semail = request.POST.get('email')
		Student.objects.create(name=sname,rollnum=srollnum,age=sage,phone=sphone,email=semail)
		#return HttpResponse("<h1>Record Added Successfully</h1>")
		return redirect('read')
	return render(request,'crud/addstudent.html')


def read(request):
	data = Student.objects.all()
	return render(request,'crud/read.html',{'data':data})



def edit(request,id):
	data = Student.objects.get(id=id)
	#return HttpResponse("Welcome to edit page")
	if request.method == "POST":
		data.name = request.POST['Studentname']
		data.rollnum = request.POST['rollnum']
		data.age = request.POST['age']
		data.phone = request.POST['phone']
		data.email = request.POST['email']
		data.save()
		return redirect('read')
		#print(data.sname)
	return render(request,'crud/update.html',{'data':data})


def Delete(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.delete()
		return redirect('read')
	return render(request,'crud/delete.html',{'info':data})







#radi,checkbox updation task
def AddNew(request):
	if request.method == "POST":
		sname = request.POST.get('Studentname')
		srollnum = request.POST.get('rollnum')
		sage = request.POST.get('age')
		sphone = request.POST.get('phone')
		semail = request.POST.get('email')
		sgender = request.POST.get('gender')
		slanguages = request.POST.getlist('lan')
		StudentNew.objects.create(name=sname,rollnum=srollnum,age=sage,phone=sphone,email=semail,gender=sgender,languages=slanguages)
		#return HttpResponse("New record added")
		return redirect('Display')
	return render(request,'crud/addstudentnew.html')


def Display(request):
	newdata = StudentNew.objects.all()
	return render(request,'crud/display.html',{'newdata':newdata})


def update(request,id):
	stu_data = StudentNew.objects.get(id=id)
	if request.method == "POST":
		stu_data.name = request.POST['Studentname']
		stu_data.rollnum = request.POST['rollnum']
		stu_data.age = request.POST['age']
		stu_data.phone = request.POST['phone']
		stu_data.email = request.POST['email']
		stu_data.gender = request.POST['gender']
		stu_data.languages = request.POST['lan']
		#print(stu_data.sname)
		stu_data.save()
		return redirect('Display')
	return render(request,'crud/updatenew.html',{'data':stu_data})



def deleteNew(request,id):
	rec = StudentNew.objects.get(id=id)
	if request.method == 'POST':
		rec.delete()
		return redirect('Display')
	return render(request,'crud/delnew.html',{'info1':rec})


