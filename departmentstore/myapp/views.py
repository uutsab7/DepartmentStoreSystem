from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import *
from . forms import *
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def index(request):
   
    orders = Order.objects.all()
    product = Product.objects.all()
    orders_count = orders.count()
    product_count = product.count()
    staff_count = User.objects.all().count()
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard:index')

    else:
        form = OrderForm()
    context ={
        'orders':orders,
        'form':form,
        'product':product,
        'orders_count':orders_count,
        'product_count':product_count,
        'workers_count':staff_count


      
        
    }
    return render(request,'dashboard/index.html',context)


@login_required(login_url='login')
def staff(request):
    orders_count = Order.objects.all().count()
    workers = User.objects.all()
    workers_count = workers.count()
    product_count = Product.objects.all().count()
    context = {
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
       
    } 
    return render(request,'dashboard/staff.html',context)

@login_required(login_url='login')
def staff_detail(request,id):
    workers = User.objects.get(id=id)
    context ={
        'workers':workers
    } 
    return render(request,'dashboard/staff_detail.html',context)

@login_required(login_url='login')
def product(request):
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    items = Product.objects.all()
    product_count = items.count()
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard:product')
            
    else:
        form = ProductForm()
    context ={
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count
        
    }

    return render(request,'dashboard/product.html',context)
@login_required(login_url='login')
def product_delete(request,id):
    item = Product.objects.get(id=id)
    if request.method =="POST":
        item.delete()
        return redirect('dashboard:product')


    return render(request,'dashboard/product_delete.html ')

@login_required(login_url='login')
def product_update(request,id):
    item = Product.objects.get(id=id)
    if request.method =='POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard:product')
    else:
        form = ProductForm(instance=item)
    context ={
        'form':form

    }
    return render(request,'dashboard/product_update.html',context)

@login_required(login_url='login')
def order(request):
    workers_count = User.objects.all().count()
    orders = Order.objects.all()
    orders_count = orders.count()
    product_count = Product.objects.all().count()
    context ={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count 
         
    }
    return render(request,'dashboard/order.html',context)
