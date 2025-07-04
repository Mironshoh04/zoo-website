from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')


def login(request):
    template_date = {}
    template_date['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {
            'template_date': template_date,
            'show_hero': False  # Don't show hero section on login page
        })
    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            template_date['error'] = 'Invalid username or password'
            return render(request, 'accounts/login.html', {
                'template_date': template_date,
                'show_hero': False  # Don't show hero section on error
            })
        else:
            auth_login(request, user)
            return redirect('home.index')


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {
            'template_data': template_data,
            'show_hero': False  # Don't show hero section on signup page
        })
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {
                'template_data': template_data,
                'show_hero': False  # Don't show hero section on error
            })
