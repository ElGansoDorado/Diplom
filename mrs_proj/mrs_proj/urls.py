# project/urls.py
from django.contrib import admin
from django.urls import path
from web_handler import views as web_handler_views
from clients.views import client_list, client_detail_by_token, delete_client  # Import the view from the clients app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("contacts/", web_handler_views.contacts),
    path("login/", web_handler_views.custom_login, name='login'),
    path('', web_handler_views.home, name='home'),
    path('dashboard/', web_handler_views.dashboard, name='dashboard'),
    path('client-detail/<str:token>/', client_detail_by_token, name='client_detail_by_token'),
    path('delete-client/<str:token>/', delete_client, name='delete_client'),

    # Include the 'clients' app view
    path('client-list/', client_list, name='client_list'),
]
