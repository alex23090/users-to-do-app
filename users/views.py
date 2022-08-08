from django.shortcuts import render, redirect
from todo_app.models import ToDoList
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def profileRegister(request):
    page = 'register'
    form = CustomUserCreationForm(request.POST)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = request.POST['email']
            name = request.POST['first_name']
            subject = 'Welcome to "To Do List" app'
            message = f'{name}, we are glad that you are here!'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            user.save()
            messages.success(request, 'User account was successfully created!')

            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'An error has occurred during registration!')

    context = {'form': form, 'page': page}
    return render(request, 'login_register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You successfully signed in!')
            return redirect('account')
        else:
            messages.error(request, "Username OR password is incorrect!")

    return render(request, 'login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was successfully logged out!')
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    todo_lists = ToDoList.objects.all().filter(owner=profile)
    context = {'profile': profile, 'todo_lists': todo_lists}
    return render(request, 'account.html', context)


@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully edited!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'edit_profile.html', context)