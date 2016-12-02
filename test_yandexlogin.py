from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from model import user
from selenium_fixture import app


def test_login(app):
    app.go_to_home_page()
    app.login(user.User.Admin())
    app.logout()