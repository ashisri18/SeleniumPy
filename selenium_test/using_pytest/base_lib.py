import pytest
from selenium import webdriver
import logging
import time
import os
import sys
from datetime import datetime

class BaseLib:
    d = os.path.dirname(os.getcwd())
    print(d)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.dirname(os.getcwd())+"\Reports\Logs.log"
    print(log_path)
    logging.basicConfig(level=logging.INFO, filename=log_path)

    @pytest.fixture()
    def resource(self):
        chromeDriver = "E:\CBT_Automation\Python_Workspace\SeleniumPy\selenium_test\chromedriver.exe"
        self.driver = webdriver.Chrome(chromeDriver)
        logging.info('Chrome browser launched.')
        # self.driver = webdriver.Firefox()
        # logging.info("Firefox browser launched")
        self.driver.get("https://www.jabong.com")
#        self.driver.get("https://ariel.auvenir.com/checkToken?token=IkMraHClAMZU2hNgsn1jKwrNr8JKpLSK&email=auvclient01@gmail.com")
        logging.info('Jabong Application Launched.')
        self.driver.maximize_window()
        logging.info("windows maximized")
        time.sleep(5)
        yield "resource"
        logging.info("Quiting driver")
        self.driver.quit()


    # @pytest.fixture()
    # def resource():
    #     print("Hello")
    #     driver = webdriver.Firefox()
    #     logging.info("Firefox browser launched")
    #     driver.get("http://www.jabong.com/")
    #     logging.info('Jabong Application Launched.')
    #     driver.maximize_window()
    #     time.sleep(3)
    #     driver.implicitly_wait(10)
    #
    #
    # def teardown_method(self, method):
    #     self.driver.quit()
    #     logging.info("Driver quited")