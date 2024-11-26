from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .models import Sensor

# Vizualizarea pentru pagina de înregistrare
# Vizualizarea pentru pagina de înregistrare
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Cont creat cu succes! Te poți autentifica acum.')
                return redirect('login')  # Redirecționare la login după înregistrare
            else:
                messages.error(request, 'Numele de utilizator există deja.')
        else:
            messages.error(request, 'Parolele nu coincid.')

    return render(request, 'register.html')

# View pentru dashboard
def dashboard(request):
    # Poți adăuga logica pentru a prelua date din baza de date
    sensors = Sensor.objects.all()  # Exemplu de preluare a tuturor senzorilor
    return render(request, 'main/dashboard.html', {'sensors': sensors})

# Vizualizarea pentru pagina de autentificare
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Autentificat cu succes!')
            return redirect('dashboard')  # Redirecționare la dashboard după autentificare
        else:
            messages.error(request, 'Nume de utilizator sau parolă incorectă.')
    
    return render(request, 'login.html')


# Vizualizarea pentru deconectare
def logout_view(request):
    logout(request)
    messages.success(request, 'Deconectat cu succes!')
    return redirect('login')  # Redirecționare la login după deconectare


# Pagina de home
@login_required
def home(request):
    return render(request, 'home.html')  # Asigură-te că ai fișierul home.html


# Pagina de dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  # Asigură-te că ai fișierul dashboard.html


# Pagina de profil
@login_required
def profil(request):
    return render(request, 'user.html')  # Asigură-te că ai fișierul user.html
