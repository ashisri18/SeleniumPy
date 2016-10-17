from selenium_test.using_pytest.base_lib import *
from selenium_test.using_pytest.pom import *
from selenium_test.using_pytest.sample1 import *

class TestScripts(BaseLib, POM):

    def test_sign_in(self, resource):
        logging.info("Inside Test")
        self.driver.find_element(*POM.SIGNIN_LINK).click()
        print("Clicked on Signin link")
        time.sleep(2)
        self.driver.find_element(*POM.EMAIL_TEXTBOX).send_keys("ashitestmail@gmail.com")
        logging.info('Login Email Id entered.')
        time.sleep(2)
        self.driver.find_element(*POM.PASSWORD_TEXTBOX).send_keys("researcher")
        logging.info('Login Password entered.')
        time.sleep(2)
        self.driver.find_element(*POM.SIGNIN_BUTTON).click()
        logging.info('Clicked on Signin button for login Jabong.')
        time.sleep(2)
        error_msg_display = self.driver.find_element(*POM.ERROR_TEXT).is_displayed()
        if error_msg_display == True:
            logging.error('Oops....We have entered incorrect login Email Id or Password.')
        time.sleep(2)
        actualMsg = self.driver.find_element(*POM.ERROR_TEXT).text
        assert actualMsg == 'Incorrect username or password.'
        logging.info('Error message verified.')
        time.sleep(2)
        self.driver.find_element(*POM.SIGNIN_GOOGLE).click()
        logging.info('Trying to login via Google account.')
        time.sleep(2)
        self.driver.find_element(*POM.GMAIL_ID_TEXTBOX).send_keys("ashitestmail@gmail.com")
        self.driver.find_element(*POM.GMAIL_ID_NEXT_BUTTON).click()
        logging.info('Gmail login Id entered.')
        time.sleep(2)
        self.driver.find_element(*POM.GMAIL_PASSWORD_TEXTBOX).send_keys("researcher")
        logging.info('Gmail login password entered.')
        time.sleep(2)
        self.driver.find_element(*POM.GMAIL_SIGNIN_BUTTON).click()
        logging.info('Clicked on Gmail Signin button.')
        time.sleep(2)
        account_loggedin = self.driver.find_element(*POM.ACCOUNT_LOGEDIN).is_displayed()
        if account_loggedin == True:
            logging.info('We have successfully logged in Jabong application.')
        time.sleep(2)
        logging.info("*****Congratulations we have successfully passed this Login to Jabong script.*****")

