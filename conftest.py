import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(request):
    request.addoption('--language', action='store', default='en', help='Choose any language: ru, en, es, fr etc.')
    