from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_password
from selenium.webdriver.common.by import By

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path="E:\\PycharmProjects\\selenium_python\\chromedriver\\chromedriver.exe",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    elem = driver.find_element(By.ID, "index_email")
    elem.clear()
    elem.send_keys("ivorycrewing@gmail.com")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")     # огонь
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)    # нажатие клавиши

    # login_button = driver.find_element(By.ID, "index_login_button").click()
    time.sleep(10)

    # news_link = driver.find_element(By.ID, "l_nwsf").click()
    # time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()