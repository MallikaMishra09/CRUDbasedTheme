from django.shortcuts import render,redirect
from mainpage.models import Student
# Create your views here.
def indexpage(request):
    z=Student.objects.all()
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['email']
        c=request.POST['password']
        x=Student(Name=a,Email=b,Password=c)
        x.save()
    return render(request,"index.html",{'z':z})
def delete(request,myid):
    x=Student.objects.get(id=myid)
    x.delete()
    return redirect('/')
def edit(request,myid):
    if request.method=="POST":
        m=request.POST['Names']
        n=request.POST['Emails']
        o=request.POST['Passwords']
        g=Student.objects.get(id=myid)
        g.Name=m
        g.Email=n
        g.Password=o
        g.save()
        z=Student.objects.all()
        return redirect(indexpage)
    return render(request,"edit.html")

