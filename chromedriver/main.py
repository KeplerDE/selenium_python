from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
# url = "https://www.instagram.com/"

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

useragent = UserAgent()              # создадим обьект класса
# чтобы передавать опции в наш браузер, нам нужно создать обьект опций
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld)")              # подмена UserAgent
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}")       # далее мы вызываем и получае рандомный клиентский адрес


driver = webdriver.Chrome(
    executable_path="/chromedriver/chromedriver_win32/chromedriver.exe",
    options=options
)


try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")                   # перейти по заданной ссылке
    time.sleep(5)
    # driver.get(url="https://vk.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.save_screenshot("2.png")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
