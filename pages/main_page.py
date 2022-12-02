import time

from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def select_type_to_filter(self):
        self.browser.find_element(*MainPageLocators.DROPDOWN_ELEMENT).click()
        self.browser.find_element(*MainPageLocators.DROPDOWN_TYPE).click()

    def filter_by_name(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME).send_keys('D')
        self.browser.find_element(*MainPageLocators.MENU_BAR).click()

    def navigation_right_left(self):
        self.browser.find_element(*MainPageLocators.RIGHT_ARROW).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.LEFT_ARROW).click()
        time.sleep(2)

    def navigation_end_beginning(self):
        self.browser.find_element(*MainPageLocators.RIGHT_DOUBLE_ARROW).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.LEFT_DOUBLE_ARROW).click()
        time.sleep(2)

    def select_page(self):
        self.browser.find_element(*MainPageLocators.PAGE_3).click()
        time.sleep(2)
