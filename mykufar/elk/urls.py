from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, CategoryViewSet, ItemViewSet, SearchItems, SearchCategories, SearchUsers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/user/<str:query>/', SearchUsers.as_view()),
    path('search/category/<str:query>/', SearchCategories.as_view()),
    path('search/item/<str:query>/', SearchItems.as_view()),
]