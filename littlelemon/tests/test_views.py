from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(title="Pizza", price=10, inventory=30)
        self.menu2 = MenuItem.objects.create(title="Burger", price=8, inventory=50)
        self.menu3 = MenuItem.objects.create(title="Salad", price=7, inventory=20)

    def test_getall(self):
        menus = MenuItem.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(str(menus.__getitem__(0)), "Pizza : 10.00")
        self.assertEqual(str(menus.__getitem__(1)), "Burger : 8.00")
        self.assertEqual(str(menus.__getitem__(2)), "Salad : 7.00")

