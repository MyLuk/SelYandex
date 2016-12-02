from selenium import webdriver
import pytest
from model import application


@pytest.fixture
def app(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return application.Application(driver)
