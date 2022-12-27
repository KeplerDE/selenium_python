from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import instagram_password, instagram_login
import pickle


# options
options = webdriver.FirefoxOptions()


options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")   # метод перезаписи

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    # options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    # driver.get("https://instagram.com/")
    # time.sleep(5)
    #
    # username_input = driver.find_element(By.NAME, "username")
    # username_input.clear()
    # username_input.send_keys(instagram_login)
    # time.sleep(5)
    #
    # password_input = driver.find_element(By.NAME, "password")
    # password_input.clear()
    # password_input.send_keys(instagram_password)
    # time.sleep(5)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)
    #
    #
    # # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{instagram_login}_cookies", "wb"))

    driver.get("https://instagram.com/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{instagram_login}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()