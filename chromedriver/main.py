from selenium import webdriver
import time
url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="/chromedriver/chromedriver_win32/chromedriver.exe")


try:
    driver.get(url=url)                   # перейти о заданной выше ссылке
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
