from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        registration_form=CustomRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,"New account created!. Login to get started!")
            return redirect('register')
    else:
         registration_form=CustomRegisterForm()
    return render(request,'user_app/register.html',{'register_form': registration_form})
                
            