from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Aaccount has been created for{username}.Continue to login')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request,'user/register.html',{'form':form})

def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method =="POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(request.FILES,instance=request.user.profile)
    context ={
        'user_form':user_form,
        'profile_form':profile_form,

    }
    return render(request,'user/profile_update.html',context)


