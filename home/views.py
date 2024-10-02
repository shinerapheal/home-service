from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . models import *
# Create your views here.
from .forms import LoginRegister, WorkerRegister, CustomerRegister

# Create your views here.
def index(request):
    return render(request,'home.html')



def customer_home(request):
    if request.method=='POST':
        city=request.POST.get('city')
        obj=customer_info(city=city)
        obj.save()
        request.session['cit']=city
    
    return render(request, 'customer_home.html')





def admin_home(request):

    data=conf.objects.all()
    return render(request,'admin_home.html',{'data':data})

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        mail= request.POST.get('mail')
        obj=user_in(email=mail)
        obj.save()
        request.session['mail']=mail


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect(admin_home)
            elif user.is_worker:
                return redirect(worker_home)
            elif user.is_customer:
                return redirect(customer_home)

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_form = WorkerRegister(request.POST, request.FILES)
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save(commit=False)
            user.is_worker = True
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login_view')
    return render(request, 'worker_register.html', {'user_form': user_form, 'worker_form': worker_form})


def customer_register(request):
    user_form = LoginRegister()
    customer_form = CustomerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        customer_form = CustomerRegister(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
           
            

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            
            messages.info(request, 'Registered Successfully')
            return redirect('login_view')
    return render(request, 'customer_register.html', {'user_form': user_form, 'customer_form': customer_form})

def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    ci=request.session['cit']
    return render(request,'service.html',{'data':ci})
def ac(request):
    ci=request.session['cit']
    if request.method=='POST':
        service=request.POST.get('service')
        obj=ac_info(service=service)
        obj.save()
        request.session['ssservice']=service
        item="ac"
        request.session['item']=item
        return redirect('/book')
    return render(request,'ac.html',{'data':ci})
def fridge(request):
    ci=request.session['cit']
    if request.method=='POST':
        service=request.POST.get('service')
        obj=fridge_info(service=service)
        obj.save()
        request.session['ssservice']=service
        item="fridge"
        request.session['item']=item
        return redirect('/book')

    return render(request,'fridge.html',{'data':ci})
def book(request):
    ci=request.session['cit']
    it=request.session['item']
    ma=request.session['mail']
    service=request.session['ssservice']


    obj=Customers.objects.filter(email=ma)

   
    





    return render(request,'book.html',{'city':ci,'service':service,'item':it,'obj':obj})
def confi(request):
     if request.method=='POST':
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        contact=request.POST.get('contact')
        item=request.POST.get('item')
        services=request.POST.get('service')
        adree=request.POST.get('adree')
        objj=conf(name=name,email=mail,contact=contact,item=item,service=services,adresee=adree)
        objj.save()
       
         
    
        return redirect("/bookstatus")
     return render(request,'book.html')

def cusreq(request):

    data=conf.objects.filter(sta="False").order_by("crea")
    obj=Worker.objects.all()
       

    

    return render(request,'customerreq.html',{'data':data,'obj':obj})
def worker_home(request):
    ma=request.session['mail']
    wo=Worker.objects.get(email=ma)
    ty=wo.name+" "+wo.contact_no
    obj=conf.objects.filter(wor=ty)
    return render(request,'worker_home.html',{'data':obj})
def wrkdet(request):
    obj=Worker.objects.all()
    
    return render(request,'workerdet.html',{'data':obj})
def bookstatus(request):
    ma=request.session['mail']
    obj=conf.objects.filter(email=ma).order_by("-crea")
    messages.success(request,"WORKER YET TO BE ASSIGNED")
    return render(request,'bookstatus.html',{'data':obj})
def alo(request):



    if request.method=='POST':
        idn=request.GET.get('idn')

        worr=request.POST.get('wor')
        obj=conf.objects.get(id=idn)
        obj.wor=worr
        obj.save()
        return redirect('/cosreq')
    
    return render(request,'customerreq.html')
def approve(request):
     

     
     id=request.GET.get('idn')
     obj=conf.objects.get(id=id)
     obj.sta='True'
     obj.save()
     return redirect("/cosreq")

def worfil(request):
    if request.method=='POST':
        wo=request.POST.get('work')
        obj=Worker.objects.filter(type=wo)
    return render(request,'workerdet.html',{'data':obj})
def cusde(request):
    data=conf.objects.all().order_by("-crea")
    obj=Worker.objects.all()
       

    

    return render(request,'cusde.html',{'data':data,'obj':obj})
def cusfil(request):
    if request.method=='POST':
        wo=request.POST.get('work')
        obj=conf.objects.filter(item=wo).order_by("crea")
    return render(request,'cusde.html',{'data':obj})


     
