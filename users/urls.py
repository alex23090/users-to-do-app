from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.profileRegister, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.userAccount, name='account'),
    path('edit-profile/', views.editProfile, name='edit-account'),
]