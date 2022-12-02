import pytest
import time

from pages.main_page import MainPage


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result_test_go_to_login_page.png')


@pytest.mark.xfail
def test_select_type_to_filter(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.select_type_to_filter()
    browser.save_screenshot('result_test_select_type_to_filter.png')


@pytest.mark.smoke
def test_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    time.sleep(2)
    browser.save_screenshot('result_test_filter_by_name.png')


@pytest.mark.smoke
def test_navigation_right_left(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.navigation_right_left()


@pytest.mark.critical
def test_navigation_end_beginning(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.navigation_end_beginning()


@pytest.mark.smoke
def test_select_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_page()
