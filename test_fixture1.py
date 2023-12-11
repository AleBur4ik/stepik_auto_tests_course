import time
import pytest
from selenium.webdriver.common.by import By
from private import LOGIN, PASSWORD


def test_guest(browser):
    browser.implicitly_wait(10)
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(LOGIN)
    browser.find_element(By.ID, 'id_login_password').send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, 'button[class="sign-form__btn button_with-loader "]').click()
    time.sleep(60)
