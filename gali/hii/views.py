from django.shortcuts import render,HttpResponse,redirect
from .models import Student
# Create your views here.
def student(request):
    return render(request,'student.html')

def readall(request):
    ob=Student.objects.all()
    return render(request,'table2.html',{'ob':ob})

def insert(request):
    if request.method=='GET':
        return render(request,'form.html')
    else:
        a=request.POST['name']
        b=request.POST['place']
        c=request.POST['phone']

        Student.objects.create(name=a,place=b,phone=c)
        return HttpResponse("inserted")

def update(request, id):
    if request.method == 'GET':
        ob = Student.objects.get(id=id)
        return render(request, 'update.html', {'ob': ob})
    else:
        a = request.POST['name']
        b = request.POST['place']
        c = request.POST['phone']
        Student.objects.filter(id=id).update(name=a, place=b, phone=c)
        return redirect('readall')

def del2(request,id):
    Student.objects.get(id=id).delete()
    return redirect('readall')
