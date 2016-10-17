from selenium.webdriver.common.by import By

class POM:

    SIGNIN_LINK = (By.XPATH, "//a[text()='Sign In']")
    EMAIL_TEXTBOX = (By.ID, "login-email")
    PASSWORD_TEXTBOX = (By.NAME, "password")
    SIGNIN_BUTTON = (By.XPATH, "//button[text()='SIGN IN']")
    ERROR_TEXT = (By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")
    SIGNIN_GOOGLE = (By.XPATH, "//a[@class='signup-g']//span[text()='sign in with google']")
    GMAIL_ID_TEXTBOX = (By.ID, "Email")
    GMAIL_ID_NEXT_BUTTON = (By.ID, "next")
    GMAIL_PASSWORD_TEXTBOX = (By.ID, "Passwd")
    GMAIL_SIGNIN_BUTTON = (By.ID, "signIn")
    ACCOUNT_LOGEDIN = (By.CLASS_NAME, "loged-in")
    CLOSE_BUTTON = (By.CLASS_NAME, "close")

    SPORTS_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-sports']")
    JERSEYS = (By.XPATH, "//div[@class='dropdown-container row']//a[text()='Jerseys']")