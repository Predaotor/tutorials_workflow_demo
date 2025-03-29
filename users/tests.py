from django.test import TestCase
from django.urls import reverse 
import pytest 
# Create your tests here.

@pytest.fixture 
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username",
        password="test_password", 
        
    )
    return "test_username", "test_password"

def test_login_users(client, test_user):
    test_username, test_password=test_user, 
    login_results=client.login(username=test_username, password=test_password)
    assert login_results==True 
    