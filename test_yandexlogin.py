from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from model.user import User
from selenium_fixture import app


def test_login_with_valid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()


def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.random())
    assert app.is_not_logged_in()