from pages.login_page import LoginPage
import time
import pytest

@pytest.mark.parametrize('link', ['http://34.141.58.52:8080/#/login', 'http://34.141.58.52:8080'])
def test_go_to_login(browser, link):
    page = LoginPage(browser, link)
    page.open()
    page.set_login()
    page.set_pass()
    page.click_submit()
    time.sleep(1)
    browser.save_screenshot('result_test_go_to_login.png')
