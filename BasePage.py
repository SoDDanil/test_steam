import metadriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self):
        self.driver = metadriver.Driver().get_webdriver()
        self.time = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver,self.time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver,self.time).until(EC.presence_of_all_elements_located(locator))