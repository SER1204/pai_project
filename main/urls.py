from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),  # Pagina principală după login
    path('dashboard/', views.dashboard, name='dashboard'),  # Pagina dashboard
    path('profil/', views.profil, name='user'),  # Profil utilizator
    path('sensors/', include('sensors.urls')),
    path('arduino/', include('arduino_app.urls')),  # Prefix pentru URL-urile aplicației
]
