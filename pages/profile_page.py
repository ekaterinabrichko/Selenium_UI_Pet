from .login_page import LoginPage
from .locators import ProfilePageLocators
import names


class ProfilePage(LoginPage):
    def log_in_user(self):
        self.set_login()
        self.set_pass()
        self.click_submit()

    def find_pets(self):
        pets = self.browser.find_elements(*ProfilePageLocators.PETS_ClASS)
        assert len(pets) > 1

    def click_add_btn(self):
        self.browser.find_element(*ProfilePageLocators.ADD_BTN).click()

    def set_pet_name(self):
        self.browser.find_element(*ProfilePageLocators.PET_NAME).send_keys(names.get_first_name())

    def select_pet_type(self):
        self.browser.find_element(*ProfilePageLocators.DROPDOWN_PET_TYPE).click()
        self.browser.find_element(*ProfilePageLocators.PET_TYPE).click()

    def save_new_pet_info(self):
        self.browser.find_element(*ProfilePageLocators.SUBMIT_NEW_PET_BTN).click()

    def cancel_new_pet_info(self):
        self.browser.find_element(*ProfilePageLocators.CANCEL_NEW_PET_BTN).click()

    def click_edit_btn(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_1_INFO_BTN).click()

    def edit_pet_name(self):
        self.browser.find_element(*ProfilePageLocators.PET_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.PET_NAME).send_keys(names.get_first_name())

    def save_edit_pet_info(self):
        self.browser.find_element(*ProfilePageLocators.SUBMIT_EDIT_PET_BTN).click()

    def delete_pet(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_2_BTN).click()
        self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE).click()