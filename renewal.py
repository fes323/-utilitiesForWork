import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


# Дружба ЭА 3000   8500   141720000000001 по 141720000008499
# Дружба ЭА 5000   1800   142720000000001 по 142720000001799
# Дружба ЗС   3000   150    541410000000001 по 541410000000149
# Дружба ЗС   5000   50    542410000000001 по 542410000000049


options = Options()
driver = webdriver.Firefox(options=options)


def login():
    driver.get('')
    try:
        enterPhone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_phone_1'))
        )
        enterPass = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_password'))
        )
    finally:
        enterPhone.send_keys('')
        enterPass.send_keys('')
        enterPass.send_keys(Keys.ENTER)
        print(f'[INFO] Авторизация прошла успешно')
        time.sleep(5)

        renewal()


def renewal():
    index = 37596
    for i in range(542410000000001, 542410000000049):

        driver.get(f'https://<django>/admin/promocode/promocodeactivationledger/{index}/change/?_changelist_filters=q%253D{i}')
        index += 1
        print(f'[INFO] Номер промокода: {i}')

        try:
            endDate = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'id_period_end_0'))
            )
        except:
            login()
        finally:
            endDate.clear()
            endDate.send_keys('11.04.2023')
            saveButton = driver.find_element('name', '_save')
            saveButton.click()


if __name__ == '__main__':
    login()