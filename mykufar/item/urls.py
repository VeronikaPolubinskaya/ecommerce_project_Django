from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
]