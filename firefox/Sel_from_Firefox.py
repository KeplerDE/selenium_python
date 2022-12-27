from selenium import webdriver
import time
from fake_useragent import UserAgent


# options
options = webdriver.FirefoxOptions()

# change useragent
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)   # метод перезаписи

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    options=options
)


try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # driver.save_screenshot("vk.png")
    time.sleep(5)
    # email_input = driver.find_element("id", "index_email")        # передаём параметром значение ай ди шника нашей испытуемыой формы
    # email_input.clear()
    # email_input.send_keys("************")
    # time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
