from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def set_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('kate.bri13@gmail.com')

    def set_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('602080Kate')

    def click_submit(self):
        login_submit = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_submit.submit()