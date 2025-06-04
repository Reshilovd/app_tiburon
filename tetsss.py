import time
import sys
import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument(
    "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/116.0.0.0 Safari/537.36'")

options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Users\\Denis.Reshilov\\Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get("https://client2.survstat.ru/#/list/0")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Login'))
    )
    login_input = driver.find_element(By.ID, 'Login')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Password'))
    )
    password = driver.find_element(By.ID, 'Password')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'login__submit'))
    )
    enter_button = driver.find_element(By.CLASS_NAME, 'login__submit')
except TimeoutException:
    print("Не найден элемент на странице авторизации")
    driver.close()
    driver.quit()
    sys.exit()

login_input.send_keys('ipsos.reshilov')
password.send_keys("o[aRlTE(66Va&12ap'Du")
enter_button.click()

driver.get("https://client2.survstat.ru/#/item/cc/10006/general")
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="form-control ng-pristine ng-valid ng-not-empty ng-touched"]'))
    )
    status = driver.find_element(By.XPATH, '//input[@class="form-control ng-pristine ng-valid ng-not-empty ng-touched"]')
    print(status)
except TimeoutException:
    print(f' не найден статус проекта...')