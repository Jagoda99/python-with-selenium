from selenium import webdriver
import pytest

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.go_to_my_account(utils.URL)
        login.login_username(utils.USERNAME)
        login.login_password(utils.PASSWORD)
        login.click_login_button()

    def test_logout(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
