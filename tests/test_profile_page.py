from pages.profile_page import ProfilePage
import time
import pytest


@pytest.mark.smoke
def test_find_existing_pets(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.find_pets()
    time.sleep(1)
    browser.save_screenshot('result_find_pet.png')


@pytest.mark.smoke
def test_add_new_pet(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.click_add_btn()
    time.sleep(1)
    page.set_pet_name()
    page.select_pet_type()
    page.save_new_pet_info()
    page.open()
    page.scroll()
    time.sleep(1)
    browser.save_screenshot('result_add_pet.png')


@pytest.mark.critical
def test_cancel_new_pet(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.click_add_btn()
    time.sleep(1)
    page.set_pet_name()
    page.select_pet_type()
    page.cancel_new_pet_info()
    page.open()
    page.scroll()
    browser.save_screenshot('result_cancel_add_pet.png')


@pytest.mark.smoke
def test_edit_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.click_edit_btn()
    time.sleep(1)
    page.edit_pet_name()
    page.save_edit_pet_info()
    page.open()
    page.refresh()
    time.sleep(1)
    browser.save_screenshot('result_edit_pet.png')


@pytest.mark.critical
def test_cancel_edit_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.click_edit_btn()
    time.sleep(1)
    page.edit_pet_name()
    page.open()
    time.sleep(1)
    browser.save_screenshot('result_cancel_edit_pet.png')


@pytest.mark.smoke
def test_delete_pet(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_in_user()
    time.sleep(1)
    page.delete_pet()
    time.sleep(1)
    browser.save_screenshot('result_delete_pet.png')
