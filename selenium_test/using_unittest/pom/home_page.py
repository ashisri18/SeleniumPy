from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
from selenium_test.using_unittest.library.base_lib import *


class HomePage(BaseLib):
    base_lib = BaseLib()

    SIGNIN_LINK = (By.XPATH, "//a[text()='Sign In']")
    MEN_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-men']")
    SPORTS_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-sports']")

    SUITE_BLAZER = (By.XPATH, "//div[@class='dropdown-container row']//a[text()='Suits & Blazers']")
    JERSEYS = (By.XPATH, "//div[@class='dropdown-container row']//a[text()='Jerseys']")

    def navigate_men(self):
        element = self.driver.find_element(self.MEN_SECTION)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)

    def click_suits_blazers(self):
        element = self.driver.find_element(self.SUITE_BLAZER)
        element.click()
        logging.info('Clicked on Suits and Blazers in Clothing category.')
        time.sleep(2)

