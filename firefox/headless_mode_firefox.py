from selenium.webdriver.common.keys import Keys
from auth_data import instagram_password, instagram_login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



# options
options = webdriver.FirefoxOptions()


# disable webdriver mode
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")   # метод перезаписи


# disable webdriver mode
# options.set_preference("dom.webdriver.enabled", False)

# headless mode
options.headless = True

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    # options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://instagram.com/")
    time.sleep(5)

    print("Passing authentication...")
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(instagram_login)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(instagram_password)
    time.sleep(5)

    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    print("Going to the post...")
    video_post = driver.get("https://www.instagram.com/reel/CmmWNsgBY-T/")
    time.sleep(10)

    print("Unmuting audio...")
    # копировать полную строку XPath для включения звука
    unmute_audio = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/button/div")
    unmute_audio.click()
    time.sleep(5)

    print("Finish watching the video...")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()