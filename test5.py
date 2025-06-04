from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_func import init_chrome_driver, auth_tiburon
import time
driver = init_chrome_driver("show")

auth_tiburon(driver, "ipsos.reshilov", "o[aRlTE(66Va&12ap'Du")

url = "https://client2.survstat.ru/#/item/ip/944/report"

driver.get(url)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="checkbox"]//label[@class="text-primary"]'))
    )

checkboxes = driver.find_elements(By.XPATH, '//div[@class="checkbox"]//label')
# //label[@class="text-primary"]
for cb in checkboxes:
    class_attr = cb.get_attribute("class")
    if "text-primary" in class_attr:
        print(1)
    else:
        print(0)
        cb.click()

time.sleep(5)
