from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import data
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def sdata(request):
    if request.method=="POST":
        name=request.POST['name']
        mname=request.POST['mname']
        fname=request.POST['fname']
        contact=request.POST['contact']
        dob=request.POST['dob']
        email=request.POST['email']
        pwd=make_password(request.POST['pswd'])
        if data.objects.filter(password=pwd).exists():
            messages.error(request,'email already exist')
        elif data.objects.filter(contact=contact).exists():
            messages.error(request,'contact already exist')
        else:
            data.objects.create(name=name,mothername=mname,fathername=fname,contact=contact,dob=dob,email=email,password=pwd)
            return render(request,'login.html')          

def login(request):
    return render(request,'login.html')

def ldata(request):
    if request.method=='POST':
        contact=request.POST['lcontact']
        ppassword=request.POST['lpassword']
        if data.objects.filter(contact=contact).exists():
            obj=data.objects.get(contact=contact)
            password=obj.password
            if check_password(ppassword,password):
                return redirect('/table/')
            else:
                messages.error(request,'Password Is Incorrect')

        else:
            messages.error(request,'contact number is not valid')

def table(request):
    table=data.objects.all()
    return render(request,'table.html',{'data':table})

def update(request,uid):
    res=data.objects.get(id=uid)
    return render(request,'update.html',{'i':res})

def updatefunction(request):
    if request.method=="POST":
        uid=request.POST['uid']
        name1=request.POST['name']
        mothername1=request.POST['mname']
        fathername1=request.POST['fname']
        dob1=request.POST['dob']
        contact1=request.POST['contact']
        email1=request.POST['email']
        data.objects.filter(id=uid).update(name=name1,mothername=mothername1,fathername=fathername1,dob=dob1,contact=contact1,email=email1)
        return redirect('/table/')
def delete(request,pk):
    use=data.objects.filter(id=pk).delete()
    return redirect('/table/')