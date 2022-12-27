from selenium import webdriver
import time
import random
from fake_useragent import UserAgent



# options, чтобы изменить UserAgent
options = webdriver.ChromeOptions()
user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]


# change useragent
useragent = UserAgent()

# user-agent
# options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")       # подставляем из списка наши юзер агенты
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(
    executable_path="E:\\PycharmProjects\\selenium_python\\chromedriver\\chromedriver.exe",
    options=options
)                # применим опции к нашему драйверу




try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)
    # email_input = driver.find_element("id", "index_email")        # передаём параметром значение ай ди шника нашей испытуемыой формы
    # email_input.clear()
    # email_input.send_keys("")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
