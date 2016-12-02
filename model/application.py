class Application(object):

    def __init__(self, driver):
        self.driver = driver

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