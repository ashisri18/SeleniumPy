from selenium.webdriver.common.by import By
from selenium_test.using_unittest.library.base_lib import *
from selenium.webdriver.common.action_chains import *


class MenPage(BaseLib):
    FILTER_SLIM = (By.XPATH, "//input[@type='checkbox' and @value='Slim']")
    SORT_FILTER = (By.XPATH), "//option[text()='Popularity']"
    SUITE_01_IMAGE = (By.XPATH, "//div[div[contains(text(),'The Design Factory ')]//span[contains(text(),'Solid Maroon  Blazer')]]"
              "/preceding-sibling::figure")
    SUITE_02_IMAGE = (By.XPATH, "//div[div[contains(text(),'Mufti')]//span[contains(text(),'Blue Jackets & Blazers')]]"
                                "/preceding-sibling::figure")
    SELECT_SIZE = (By.XPATH, "//ul[@class='options']//li[contains(@class,'first popover-options')]")
    ADD_TO_BAG = (By.ID, "add-to-cart")
    BAG_ICON = (By.ID, "mini-cart")
    REMOVE_BUTTON = (By.XPATH, "//a[text()='REMOVE']")


    def scroll_down(self):
        element = self.driver.find_element(self.FILTER_SLIM)
        ActionChains(self.driver).move_to_element(element).perform()
        logging.info('Scrolled down to Filter out products.')
        time.sleep(2)

    def click_filter_slim(self):
        element = self.driver.find_element(self.FILTER_SLIM)
        element.click()
        logging.info('Clicked on Slim in Filter category.')
        time.sleep(2)

    def open_blazer(self):
        element = self.driver.find_element(self.SUITE_02_IMAGE)
        element.click()
        logging.info("Product opened to see it's details.")
        time.sleep(2)

    def select_size(self):
        select_size = self.driver.find_element(self.SELECT_SIZE)
        select_size.click()
        logging.info('Size is selected for the product.')
        time.sleep(2)

    def click_add_to_bag(self):
        add_to_bag_button = self.driver.find_element(self.ADD_TO_BAG)
        add_to_bag_button.click()
        logging.info('Clicked to add product in Cart')
        time.sleep(10)

    def click_bag_icon(self):
        bag_icon = self.driver.find_element(self.BAG_ICON)
        # ActionChains.move_to_element(bag_icon).perform()
        bag_icon.click()
        logging.info('Clicked on Bag icon and Product is successfully added to Cart.')
        time.sleep(5)

    def click_remove_button(self):
        remove_button = self.driver.find_element(self.REMOVE_BUTTON)
        remove_button.click()
        logging.info('Product removed from Cart.')
        time.sleep(2)