from selenium_test.using_unittest.pom.men_page import *
from selenium_test.using_unittest.pom.home_page import *
from selenium.common.exceptions import *
import traceback
from selenium.webdriver.common.action_chains import ActionChains


class BuyProduct(HomePage, MenPage, BaseLib):

    @pytest.mark.run(order=1)
    def test_buy_jersey(self):
        test_method_name = self._testMethodName
        try:
            logging.info("Inside test_buy_jersey")
            element = self.driver.find_element(*HomePage.SPORTS_SECTION)
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(2)
            logging.info("Clicked on Sports section")
            self.driver.find_element(*HomePage.JERSEYS).click()
            logging.info("Clicked on Jersey")
            time.sleep(2)
        except:
            logging.error('Exception raised in method - test_buy_jersey')
            # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(BaseLib.d + "Reports\Screenshots\\" + test_method_name + "-" + BaseLib.now + ".png")
            traceback.print_exc()
            logging.info("test_buy_jersey =" + "Fail")
            raise WebDriverException

    @pytest.mark.run(order=2)
    def test_buy_blazers(self):
        test_method_name = self._testMethodName
        try:
            home_page = HomePage()
            men_page = MenPage()

            logging.info('Now in Men Script')
            home_page.navigate_men()
            home_page.click_suits_blazers()
            men_page.scroll_down()
            men_page.click_filter_slim()
            men_page.open_blazer()
            men_page.select_size()
            men_page.click_add_to_bag()
            men_page.click_bag_icon()
            men_page.click_remove_button()
            logging.info(test_method_name + "=" + "Pass")

        except WebDriverException:
            logging.error('Exception raised in method - ' + test_method_name)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(BaseLib.d + "Reports\Screenshots\\" + test_method_name + "-" + now + ".png")
            traceback.print_exc()
            logging.info(test_method_name + "=" + "Fail")
            raise WebDriverException