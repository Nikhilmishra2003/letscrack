from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Password not match")

        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            return HttpResponse("invalid username or password")
    else:
        next_url = request.GET.get('next')
        if next_url and request.user.is_authenticated:
            return redirect(next_url)
        else:
            return render(request, 'login.html')


            # Render the login page

# @login_required(login_url='login')
# @login_required
def HomePage(request):
    return render(request, 'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def find_out_more(request):
    return render(request, 'find_out_more.html')

# @login_required
def find_out_more_1(request):
    return render(request, 'find_out_more_1.html')

def find_out_more_2(request):
    return render(request, 'find_out_more_2.html')

def find_out_more_3(request):
    return render(request, 'find_out_more_3.html')

def another_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('find_out_more_1'))
    else:
        # Render the login page or handle as desired if the user is not logged in
        return render(request, 'login.html')


def my_view(request):
    user = request.user
    return render(request, 'index .html', {'user': user})