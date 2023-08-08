from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congratulations {username}! you can now login!')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    context = {            
        'form' : form ,
        'title' : 'Register',
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    return render(request, 'user/profile.html')