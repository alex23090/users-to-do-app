from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView, name='home'),

    path('create-list/', views.CreateListView, name='create-list'),
    path('list/<str:pk>/', views.ViewList, name='list'),
    path('delete-list/<str:pk>/', views.DeleteList, name='delete-list'),
    path('update-list/<str:pk>/', views.UpdateList, name='update-list'),

    path('add-item/<str:pk>/', views.CreateItemView, name='add-item'),
    path('update-item/<str:pk>/', views.UpdateItem, name='update-item'),
    path('delete-item/<str:pk>/', views.DeleteItem, name='delete-item'),
]