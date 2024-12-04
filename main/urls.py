from django.urls import path
from django.views.generic import RedirectView  # Import RedirectView
from main.views import login_user, register, logout_user
from main.views import show_auth, show_mainpage
from main.views import login, register_flutter

app_name = 'main'

urlpatterns = [
    path('', show_auth, name='show_auth'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('mainpage/', show_mainpage, name='show_mainpage'),
    path('login_flutter/', login, name='login_flutter'),
    path('register_flutter/', register_flutter, name='register_flutter')
]