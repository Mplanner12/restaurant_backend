from django.http import JsonResponse
from .models import MenuItem
from rest_framework import generics # type: ignore
from .serializers import MenuItemSerializer

class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

def menu_list(request):
    menu_items = MenuItem.objects.all().values('id', 'name', 'description', 'price')
    return JsonResponse(list(menu_items), safe=False)

