from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_name = "username"
        self.password_name = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def go_to_my_account(self, url):
        self.driver.get(url)

    def login_username(self, username):
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)

    def login_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
