from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import RegistrationForm, LoginForm, ProfileForm, UserForm
from account.models import Profile


def get_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'profile.html',
                      {"user": user,  "is_admin": request.user.is_superuser, "is_own": True}
                      )
    return redirect('/login')


def edit_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile')
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html',
                  {"user": user, "is_own": False}
                  )


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            account = Profile(user=user)
            user.save()
            account.save()
            return redirect('/login')
    form = RegistrationForm()
    return render(request, 'register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/posts')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/posts')
