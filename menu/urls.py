from django.urls import path
from . import views
from .views import MenuItemListCreate

urlpatterns = [
    path('menu/', views.menu_list),
]

urlpatterns = [
    path('menu-items/', MenuItemListCreate.as_view(), name='menu-item-list-create'),
]
