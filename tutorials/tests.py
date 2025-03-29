from django.test import TestCase
from django.urls import reverse 
from tutorials.models import Tutorial
import pytest 
# Create your tests here.

def test_homepage():
    url=reverse('home')
    assert url=="/"
    
@pytest.fixture
def new_tutorial(db):
    tutorial=Tutorial.objects.create(
        title='Pytest',
        tutorial_url="http://pytest-django-readthedocs.io/en/latest/index.html",
        description="Tutorial how to apply pytets",
        published=True
    )
    return tutorial

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()
    
def test_update_tutorial(new_tutorial):
    new_tutorial.title="Pytest-django"
    new_tutorial.save()
    assert Tutorial.objects.filter(title="Pytest-django").exists()
    
@pytest.fixture
def another_tutorial(db):
    tutorial=Tutorial.objects.create(
        title="More-pytest",
        tutorial_url="http://pytest-django-readthedocs.io/en/latest/index.html",
        description="Another tutorial",
        published=True
    )
    return tutorial
    
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk