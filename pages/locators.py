from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    DROPDOWN_TYPE = (By.XPATH, "//*[@id='pv_id_2']/div/span")
    DROPDOWN_ELEMENT = (By.ID, "pv_id_2_1")
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    MENU_BAR = (By.XPATH, '//*[@id="app"]/header/div')
    RIGHT_ARROW = (By.XPATH, "//*[@id='app']/main/div/div[2]/div[3]/button[3]/span")
    RIGHT_DOUBLE_ARROW = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[4]/span')
    LEFT_ARROW = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[2]/span')
    LEFT_DOUBLE_ARROW = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[1]/span')
    PAGE_3 = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/span/button[3]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    PETS_ClASS = (By.CSS_SELECTOR, ".col-12")
    ADD_BTN = (By.XPATH, "//*[@id='app']/main/div/div/div[1]/div/div[1]/button/span[1]")
    PET_NAME = (By.ID, 'name')
    DROPDOWN_PET_TYPE = (By.XPATH, '//*[@id="pv_id_4"]')
    PET_TYPE = (By.ID, 'pv_id_4_2')
    SUBMIT_NEW_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CANCEL_NEW_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]')
    EDIT_PET_1_INFO_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    SUBMIT_EDIT_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
    DELETE_PET_2_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[2]/div/div[2]/button[2]')
    CONFIRM_DELETE = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
