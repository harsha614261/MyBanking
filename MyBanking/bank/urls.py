from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('safe',views.safe,name='safe'),
    path('logout',views.logout,name='logout'),
    path('Message',views.Message,name='Message'),
    path('addfunds',views.addfunds,name='addfunds'),
    path('balance',views.balance,name="balance"),
    path('statements',views.statements,name="statements"),
    path('transfer',views.transfer,name='transfer'),
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]
