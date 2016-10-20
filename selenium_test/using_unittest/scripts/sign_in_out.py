from selenium_test.using_unittest.library.base_lib import *
from selenium_test.using_unittest.pom.home_page import *
from selenium_test.using_unittest.pom.signin_page import *
from selenium.common.exceptions import *
import traceback


class SignInOut(HomePage, BaseLib, SigninPage):

    def test_sign_in(self):

        try:
            logging.info("Inside test_sign_in")
            self.driver.find_element(*HomePage.SIGNIN_LINK).click()
            logging.info("Clicked on Signin link")
            time.sleep(2)
            self.driver.find_element(*SigninPage.EMAIL_TEXTBOX).send_keys("ashitestmail@gmail.com")
            logging.info('Login Email Id entered.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.PASSWORD_TEXTBOX).send_keys("researcher")
            logging.info('Login Password entered.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.SIGNIN_BUTTON).click()
            logging.info('Clicked on Signin button for login Jabong.')
            time.sleep(2)
            error_msg_display = self.driver.find_element(*SigninPage.ERROR_TEXT).is_displayed()
            if error_msg_display == True:
                logging.error('Oops....We have entered incorrect login Email Id or Password.')
            time.sleep(2)
            actualMsg = self.driver.find_element(*SigninPage.ERROR_TEXT).text
            assert actualMsg == 'Incorrect username or password.'
            logging.info('Error message verified.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.SIGNIN_GOOGLE).click()
            logging.info('Trying to login via Google account.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.GMAIL_ID_TEXTBOX).send_keys("ashitestmail@gmail.com")
            self.driver.find_element(*SigninPage.GMAIL_ID_NEXT_BUTTON).click()
            logging.info('Gmail login Id entered.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.GMAIL_PASSWORD_TEXTBOX).send_keys("researcher")
            logging.info('Gmail login password entered.')
            time.sleep(2)
            self.driver.find_element(*SigninPage.GMAIL_SIGNIN_BUTTON).click()
            logging.info('Clicked on Gmail Signin button.')
            time.sleep(2)
            account_loggedin = self.driver.find_element(*SigninPage.ACCOUNT_LOGEDIN).is_displayed()
            if account_loggedin == True:
                logging.info('We have successfully logged in Jabong application.')
            time.sleep(2)
            logging.info("*****Congratulations we have successfully passed this Login to Jabong script.*****")

        except WebDriverException:
            logging.error('Exception raised in method - test_sign_in')
            # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(BaseLib.d + "\Reports\\" + "test_sign_in.png")
            traceback.print_exc()
            logging.info("test_sign_in =" + "Fail")
            raise WebDriverException