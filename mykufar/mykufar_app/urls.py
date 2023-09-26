from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'mykufar_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    # path('products_by_user/', views.products_by_user, name='products_by_user'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # path('products', views.products, name='products'),
    # path('new_product/', views.new_product, name='new_product'),
    # path('<int:pk>/', views.product_detail, name='product_detail'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # path('product_view/', views.ProductViewSet.as_view({'get': 'list'}), name='product_view'),
    # path('category_view/', views.CategoryViewSet.as_view({'get': 'list'}), name='category_view'),
    # path('user_list/<int:user_id>/', views.user_list, name='user_list'),
]