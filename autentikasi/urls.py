from django.urls import path
from django.views.generic import RedirectView  # Import RedirectView
from autentikasi.views import show_main_user, show_main_seller
from autentikasi.views import create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from autentikasi.views import register_user, register_seller
from autentikasi.views import login_user, login_seller
from autentikasi.views import logout_user, logout_seller

app_name = 'autentikasi'

urlpatterns = [
    path('', RedirectView.as_view(url='login/user/')),  # Redirect root URL to login page
    path('user/', show_main_user, name='show_main_user'),
    path('seller/', show_main_seller, name='show_main_seller'),
    path('create-mood-entry/', create_mood_entry, name='create_mood_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/user/', register_user, name='register_user'),
    path('register/seller/', register_seller, name='register_seller'),
    path('login/user/', login_user, name='login_user'),
    path('login/seller/', login_seller, name='login_seller'),
    path('logout/user/', logout_user, name='logout_user'),
    path('logout/seller/', logout_seller, name='logout_seller'),
]

