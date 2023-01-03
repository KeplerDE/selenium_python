from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_password, vk_email
from selenium.webdriver.common.by import By
import pickle



# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

#headless mode
options.add_argument('--headless')          # первый способ
options.headless = True                     # второй способ

driver = webdriver.Chrome(
    executable_path="E:\\PycharmProjects\\selenium_python\\chromedriver\\chromedriver.exe",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://vk.com/")
    time.sleep(5)
    print("Passing authentication...")

    elem = driver.find_element(By.ID, "index_email")
    elem.clear()
    elem.send_keys(vk_email)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")     # огонь
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)    # нажатие клавиши

    # driver.get("https://vk.com/")
    time.sleep(7)

    print("Going to the profile page...")
    profile_page = driver.find_element(By.ID, "l_pr").click()           # зашли на главную страничку
    time.sleep(5)


    print("Start watching the video...")
    video_block = driver.find_element(By.CLASS_NAME, 'wall_text').click()     # клик на видео
    time.sleep(15)
    print("Finish watching the video...")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
