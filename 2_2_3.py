import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# создаем тестовый файл
with open('abc.txt', 'w', encoding='utf-8') as file:
    file.write('1234567890 qwerty')

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'abc.txt')

with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get('https://suninjuly.github.io/file_input.html')
    for i in browser.find_element(By.CLASS_NAME, 'form-group').find_elements(By.CSS_SELECTOR,
                                                                             'input'):
        i.send_keys('aaa')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    print(browser.switch_to.alert.text.split()[-1])

os.remove(file_path)  # удаляем тестовый файл
