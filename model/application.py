from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(driver, 10)

    def login(self, user):
        driver=self.driver
        driver.find_element_by_name('login').send_keys(user.username)
        driver.find_element_by_name('passwd').send_keys(user.password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def logout(self):
        driver = self.driver
        # element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@title='jonrokf@yandex.ru']")))
        driver.find_element_by_xpath("//div[@title='jonrokf@yandex.ru']").click()
        # element2=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-metric='Меню сервисов:Выход']")))
        driver.find_element_by_xpath("//a[@data-metric='Меню сервисов:Выход']").click()

    def go_to_home_page(self):
        self.driver.get('http://yandex.ru')

    def is_logged_in(self):
        driver=self.driver
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Входящие']")))
            return True
        except WebDriverException:
            return False

    def is_not_logged_in(self):
        driver=self.driver
        try:
            self.wait.until(EC.presence_of_element_located((By.NAME, 'login')))
            return True
        except WebDriverException:
            return False


