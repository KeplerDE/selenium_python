from selenium import webdriver
import time

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)        # опция выключена и не работает

driver = webdriver.Firefox(
    executable_path="E:\PycharmProjects\selenium_python\firefox\geckodriver.exe",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()