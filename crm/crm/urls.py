
from django.contrib import admin
from django.urls import path,include
from core.views import index,about
from userprofile.views import signup
from django.contrib.auth import views

urlpatterns = [
    path('',index,name='index'),
    path('dashboard/leads/',include('lead.urls')),
    path('signup/',signup, name='signup'),
    path('dashboard/',include('dashboard.urls')),
    path('log-in/',views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('log-out/',views.LogoutView.as_view(),name='logout'),
    path('about',about,name='about'),
    path('admin/', admin.site.urls),
]
