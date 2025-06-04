import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from secondary_func import error_checker


@error_checker
def init_chrome_driver(mode="hide"):
    options = webdriver.ChromeOptions()
    webdriver.ChromeOptions()
    if mode == "hide":
        options.add_argument('--headless=new')

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "--user-agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
        "like Gecko)"
        "Chrome/119.0.0.0 Mobile Safari/537.36 Edg/119.0.0.0'")
    options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\Denis.Reshilov\\Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    return webdriver.Chrome(options=options)


@error_checker
def auth_tiburon(driver, login, password):
    url = 'https://auth.survstat.ru/login/tu9v4wzT4N?r=https%3A%2F%2Fclient2.survstat.ru%2F%23%2Flist%2F0'
    driver.get(url)

    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'g-recaptcha'))
        )
        captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
        if captcha:
            driver.close()
            driver.quit()

            return "CAPTСHA"
    except Exception as ex:
        print(ex)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Login'))
    )
    login_input = driver.find_element(By.ID, 'Login')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Password'))
    )
    password_input = driver.find_element(By.ID, 'Password')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'login__submit'))
    )
    enter_button = driver.find_element(By.CLASS_NAME, 'login__submit')

    login_input.send_keys(login)
    password_input.send_keys(password)
    time.sleep(5)
    enter_button.click()
    time.sleep(5)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="validation"]')))

        validation = driver.find_element(By.XPATH, '//div[@class="validation"]').text

        if "password" in validation:
            return "Неверный логин или пароль"
    except TimeoutException as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    return 1


@error_checker
def download_base_from_tiburon(driver, url, params_list):
    print("driver ", driver)
    print("url ", url)
    print("params_list ", params_list)
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//h5[@class="panel-title clearfix"]//span[@class="text-thin pad-left pad-right"]'))
    )
    # буду опеределять номер проекта по файлу с базой
    # project_number = driver.find_element(By.XPATH,
    #                                      '//h5[@class="panel-title clearfix"]//span[@class="text-thin pad-left '
    #                                      'pad-right"]').text

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//div[class="checkbox"]'))
    # )

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//span[text()="Данные в кодировке UTF-8"]'))
    # )
    # utf_8_checkbox_rod = driver.find_element(By.XPATH, '//span[text()="Данные в кодировке UTF-8"]')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="checkbox"]//label'))
    )
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="checkbox"]//label')
    for index, cb in enumerate(checkboxes):
        class_attr = cb.get_attribute("class")
        if params_list[index] == "1" and "text-primary" not in class_attr:
            cb.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//table[@class ="table table-condensed table-bordered table-nomargin table-vmiddle"]'))
    )

    table = driver.find_element(By.XPATH,
                                '//table[@class ="table table-condensed table-bordered table-nomargin '
                                'table-vmiddle"]')

    count_row_before_click = len(table.find_elements(By.XPATH, '//tr'))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
    )
    unloading_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    unloading_button.click()

    time.sleep(10)  # необходимо ждать когда появится новая строка, можно считать сколько было изначально и
    # сранивать

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//table[@class ="table table-condensed table-bordered table-nomargin table-vmiddle"]'))
    )

    table = driver.find_element(By.XPATH,
                                '//table[@class ="table table-condensed table-bordered table-nomargin '
                                'table-vmiddle"]')

    count_row_after_click = len(table.find_elements(By.XPATH, '//tr'))

    if count_row_after_click > count_row_before_click:
        WebDriverWait(table, 1500).until(
            EC.presence_of_element_located(
                (By.XPATH, '//tr[1]//span[@class="glyphicon glyphicon-download-alt hover-glow"]'))
        )

        # WebDriverWait(driver, 1500).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//table//tr[1]//span[@class="glyphicon glyphicon-download-alt hover-glow"]'))
        # )

        # download_button = (table.find_element(By.XPATH,
        #                                       '//tr[1]//span[@class="glyphicon glyphicon-download-alt '
        #                                       'hover-glow"]//ancestor::a'))

        download_button = (table.find_element(By.XPATH,
                                              '//tr[1]//span[@class="glyphicon glyphicon-download-alt hover-glow"]'))
        download_button.click()

        # return project_number
        return 1
