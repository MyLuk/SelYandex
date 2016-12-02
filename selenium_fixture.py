from selenium import webdriver
import pytest
from model.application import Application


@pytest.fixture(scope="module")
def app(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver)
