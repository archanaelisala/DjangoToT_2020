from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
	return HttpResponse("<h1>Welcome django Page</h1>")

def about(request):
	return HttpResponse("<h2 style='background-color:pink'> Hellooo.....</h2>")

def String(y,name):
	return HttpResponse("<h2>Hii Welcome to online class {}</h2>".format(name))

#Day1 Task
def table(h,num):
	k = ""
	for i in range(1,11):
		k += " {} X {:02} = {:02}".format(num,i,num*i)+"<br/>"
	#print(k)
	return HttpResponse(k)

#Task2
def twoVar(request,name1,age):
	#return HttpResponse("<h1> Welcome to this Page</h1>"+name1+"<h1>Age is</h1> %d"+age)
	print(name1,age)
	return render(request,'fy/index.html',{'n':name1,'a':age})


def cssexample(request):
	return render(request,'fy/demo.html')



def Login(request):
	return render(request,'fy/login.html')

def Register(request):
	return render(request,'fy/register.html')



def Javascript_Ex(request):
	return render(request,'fy/math.html')



def LoginRegister(request):
	return render(request,'fy/loginregister.html')

def boost(request):
	return render(request,'fy/bootstrap.html')