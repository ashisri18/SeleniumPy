import pytest
import unittest
from selenium import webdriver
import logging
import time
import os
import sys
from datetime import datetime


class BaseLib(unittest.TestCase):
    driver = None
    d = os.path.dirname(os.getcwd())
    print(d)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.dirname(os.getcwd())+"\Reports\\Logs"+now+".log"
    print(log_path)
    logging.basicConfig(level=logging.INFO, filename=log_path)


    @classmethod
    def setup_class(cls):
        logging.info("************************************** Execution Starts ************************************************************")
        chrome_driver_path = "E:\CBT_Automation\Python_Workspace\SeleniumPy\selenium_test\chromedriver.exe"
        cls.driver = webdriver.Chrome(chrome_driver_path)
        logging.info('Chrome browser launched.')
        cls.driver.get("http://www.jabong.com")
        logging.info('Jabong Application Launched.')
        cls.driver.maximize_window()
        logging.info("windows maximized")
        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        logging.info("Driver quited")


    # @pytest.fixture(autouse=True)
    # def _environment(request):
    #     request.config._environment.append(('foo', 'bar'))
    #
    #
    # @pytest.mark.hookwrapper
    # def pytest_runtest_makereport(item, call):
    #     pytest_html = item.config.pluginmanager.getplugin('html')
    #     outcome = yield
    #     report = outcome.get_result()
    #     extra = getattr(report, 'extra', [])
    #     if report.when == 'call':
    #         # always add url to report
    #         extra.append(pytest_html.extras.url('http://www.example.com/'))
    #         xfail = hasattr(report, 'wasxfail')
    #         if (report.skipped and xfail) or (report.failed and not xfail):
    #             # only add additional html on failure
    #             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
    #         report.extra = extra

#     @pytest.fixture(scope='function', autouse=True)
#     def resource(self):
#         logging.info("************************************** Execution Starts ************************************************************")
#         chrome_driver_path = "E:\CBT_Automation\Python_Workspace\SeleniumPy\selenium_test\chromedriver.exe"
#         self.driver = webdriver.Chrome(chrome_driver_path)
#         logging.info('Chrome browser launched.')
#         # self.driver = webdriver.Firefox()
#         # logging.info("Firefox browser launched")
#         self.driver.get("http://www.jabong.com")
# #        self.driver.get("https://ariel.auvenir.com/checkToken?token=IkMraHClAMZU2hNgsn1jKwrNr8JKpLSK&email=auvclient01@gmail.com")
#         logging.info('Jabong Application Launched.')
#         self.driver.maximize_window()
#         logging.info("windows maximized")
#         time.sleep(5)
#         yield "resource"
#         logging.info("Quiting driver")
#         self.driver.quit()
#
#         return self.driver

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
