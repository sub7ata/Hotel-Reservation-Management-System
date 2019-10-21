from django.test import TestCase
from .models import Manager

class ManagerTest(TestCase):
    def setUp(self):
        name=Manager.objects.create(name='salman')



# Create your tests here.
