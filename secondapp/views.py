from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def newlogin(request):


	if request.method == "POST":
		u = request.POST['usname']
		p = request.POST['pswd']

		#print(u,p)   #for printing values in server
		#return HttpResponse("Hi Your Username is: {}".format(u)) #passing value to the browser
		#return render(request,'scd/details.html',{'us':u,'ps':p}) #passing values to the html page
		
		#Validation
		if u == "archanaelisala@gmail.com" and p == "anu@123":
			return HttpResponse("<h1>Hi Welcome ypur username is</h1>: {}".format(u))
		else:
			return HttpResponse("Invalid Credentials")
	return render(request,'scd/login1.html')






def regi(request):
	if request.method == 'POST':
		fname = request.POST['Fname']
		lname = request.POST['Lname']
		phone = request.POST['Phone']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		#print(fname,lname)
		#return HttpResponse("ur fname is: {} and ur lname is {}".format(fname,lname))
		return render(request,'scd/registereddetails.html',{'fname':fname,'lname':lname,'phone':phone,'email':email})
	return render(request,'scd/register1.html')