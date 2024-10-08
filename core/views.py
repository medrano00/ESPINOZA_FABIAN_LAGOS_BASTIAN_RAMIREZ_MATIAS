from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Usuario creado'
            return redirect('login')
        else:
            msg = 'Formulario invalido'
    else:
        form = SignUpForm()
    return render(request, 'core/register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_parvularia:
                login(request, user)
                return redirect('parvularia')
            elif user is not None and user.is_apoderado:
                login(request, user)
                return redirect('apoderado')
            elif user is not None and user.is_superuser:
                login(request, user)
                return redirect('index')
            else:
                msg = 'Usuario o contraseña incorrectos'
        else:
            msg = 'Formulario invalido'
    return render(request, 'core/login.html', {'form': form, 'msg': msg})

def parvularia(request):
    return render(request, 'core/parvularia.html')

def apoderado(request):
    return render(request, 'core/apoderado.html')

def perfilNiño(request):
    user = request.user
    
    if not user.is_apoderado:
        return HttpResponse("Solo los apoderados pueden acceder a esta página.")
    
    try:
        apoderado = User.apoderado
    except Apoderado.DoesNotExist:
        # Manejar el caso en que no hay un Apoderado asociado
        return HttpResponse("No se ha registrado ningún Apoderado para este usuario.")
    niño = Apoderado.niño  # Obtenemos el niño asociado al apoderado
    return render(request, 'core/perfilNiño.html', {'apoderado': apoderado,'niño': niño})

def logout_view(request):
    logout(request)
    return redirect('index')