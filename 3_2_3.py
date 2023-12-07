import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestA(unittest.TestCase):
    def open_browser(self, link):
        with webdriver.Chrome() as browser:
            browser.implicitly_wait(10)
            browser.get(link)
            for i in ['.first', '.second', '.third']:
                browser.find_element(By.CSS_SELECTOR, f'.first_block {i}').send_keys('aaa')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            return welcome_text_elt.text

    def test_abc1(self):
        link = 'https://suninjuly.github.io/registration1.html'
        self.assertEqual(self.open_browser(link),
                         "Congratulations! You have successfully registered!")

    def test_abc2(self):
        link = 'https://suninjuly.github.io/registration2.html'
        self.assertEqual(self.open_browser(link),
                         "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()
