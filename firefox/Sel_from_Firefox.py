from selenium import webdriver
import time


# # options
# options = webdriver.ChromeOptions()
#
# # user-agent
# options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    # options=options
)


try:
    driver.get("https://vk.com/")
    driver.save_screenshot("vk.png")
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
