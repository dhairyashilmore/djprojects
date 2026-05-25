from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('chat/', views.chat_respond, name='chat_respond'),
]