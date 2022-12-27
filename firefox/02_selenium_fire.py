from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# options
options = webdriver.FirefoxOptions()


options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")   # метод перезаписи

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    # options=options
)


try:
    driver.get("https://instagram.com/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys("python2day")
    time.sleep(5)

    # password_input = driver.find_element(By.NAME, "password")
    # password_input.clear()
    # password_input.send_keys(instagram_password)
    # time.sleep(5)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# убрать куки