# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .models import form,form1,form2



# Create your views here.
def  login(request):
    return render(request,'management/base/login.html')



def index(request):

    return render(request, 'management/index.html')
    
def  course(request):
    return render(request,'management/admin/course.html')
def  home(request):
    return render(request,'management/admin/home.html')
def  student(request):
    return render(request,'management/admin/student.html')
def teacher(request):
    return render(request,'management/admin/teacher.html')
def about(request):
    return render(request,'management/about.html')

def data(request):
    data_value=form.objects.all()
    return render(request,'management/report/data.html',{'data':data_value})

def delete(request,id):
    form.objects.filter(id=id).delete()
    return redirect(data)
def edit(request,id):
    form_data=form.objects.filter(id=id).get()
    return render(request,'management/admin/student.html',{'form_data':form_data})

def save(request):
    
    if  request.method=='POST':
        hid=request.POST['hid']
        name=request.POST['name']
        if not name:
            msg="name feild is empty"
            return render(request,'management/admin/student.html',{'error':msg})
        email=request.POST['email']
        age=request.POST['age']
        address=request.POST['address']
        username=request.POST['username']
        
        if hid != "":
            form_ob=form.objects.filter(id=hid).get()
            form_ob=form()
            form_ob.name=name
            form_ob.email=email
            form_ob.age=age
            form_ob.address=address
            form_ob.username=username
            
            form_ob.save()
            return HttpResponse("updation")
        else:
            form_ob=form()
            form_ob.name=name
            form_ob.email=email
            form_ob.age=age
            form_ob.address=address
            form_ob.username=username
            
            form_ob.save()
            
            msg2="data inserted successfully"
            return render(request,'management/admin/student.html',{'msg1':msg2})
            
            
         
    else:
        return HttpResponse("error")

def data1(request):
    data_value=form1.objects.all()
    return render(request,'management/report/data1.html',{'data':data_value})

def delete1(request,id):
    form1.objects.filter(id=id).delete()
    return redirect(data1)
def edit1(request,id):
    form_data=form1.objects.filter(id=id).get()
    return render(request,'management/admin/teacher.html',{'form_data':form_data})

def save1(request):
    
    if  request.method=='POST':
        hid=request.POST['hid']
        name=request.POST['name']
        if not name:
            msg="name feild is empty"
            return render(request,'management/admin/teacher.html',{'error':msg})
        email=request.POST['email']
        age=request.POST['age']
        
        username=request.POST['username']
        
        if hid != "":
            form1_ob=form1.objects.filter(id=hid).get()
            form1_ob=form1()
            form1_ob.name=name
            form1_ob.email=email
            form1_ob.age=age
            
            form1_ob.username=username
            
            form1_ob.save()
            return HttpResponse("updation")
        else:
            form1_ob=form1()
            form1_ob.name=name
            form1_ob.email=email
            form1_ob.age=age
            
            form1_ob.username=username
            
            form1_ob.save()
            
            msg2="data inserted successfully"
            return render(request,'management/admin/teacher.html',{'msg1':msg2})
            
            
         
    else:
        return HttpResponse("error")

def data2(request):
    data_value=form2.objects.all()
    return render(request,'management/report/data2.html',{'data':data_value})

def delete2(request,id):
    form2.objects.filter(id=id).delete()
    return redirect(data2)
def edit2(request,id):
    form_data=form2.objects.filter(id=id).get()
    return render(request,'management/admin/course.html',{'form_data':form_data})

def save2(request):
    
    if  request.method=='POST':
        hid=request.POST['hid']
        name=request.POST['name']
        if not name:
            msg="name feild is empty"
            return render(request,'management/admin/course.html',{'error':msg})
        
        
        address=request.POST['address']
        
        age=request.POST['age']
        
        if hid != "":
            form2_ob=form2.objects.filter(id=hid).get()
            form2_ob=form2()
            form2_ob.name=name
            
            
            form2_ob.address=address
            
            form2_ob.age=age
            
            form2_ob.save()
            return HttpResponse("updation")
        else:
            form2_ob=form2()
            form2_ob.name=name
            
            form2_ob.address=address
            
            
            form2_ob.age=age
            
            form2_ob.save()
            
            msg2="data inserted successfully"
            return render(request,'management/admin/course.html',{'msg1':msg2})
            
            
         
    else:
        return HttpResponse("error")

