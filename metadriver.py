from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config_utils import OpenJson
from singleton import MetaSingleton


class Driver(metaclass=MetaSingleton):
    driver = None
    
    def WebDriver(self,chrome_options):
        if self.driver == None:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options,options = {"Steam_Language" :OpenJson.get_json().get("Steam_Language") })
        return self.driver
     
    def get_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument(OpenJson.get_json().get("mode"))
        return Driver().WebDriver(chrome_options)
    def go_to_site(self):
        self.base_url = OpenJson.get_json().get("url")
        return self.driver.get(self.base_url)  
    @classmethod
    def clean(cls):
        cls._instances= {}

    def close_driver(self):
        self.clean()
        self.driver.quit()

driver_single = Driver()
driver_single.get_webdriver()
