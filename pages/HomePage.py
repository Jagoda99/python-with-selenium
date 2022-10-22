from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = "//span[@class='oxd-userdropdown-tab']"
        self.logout_link_xpath = "//a[normalize-space()='Logout']"

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()
