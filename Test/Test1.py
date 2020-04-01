from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\\Users\\Elven\\PycharmProjects\\Test1\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("http://amazon.com.mx")

time.sleep(8)
driver.find_element_by_name("field-keywords").send_keys("Videojuegos")
time.sleep(4)
driver.find_element_by_name("field-keywords").send_keys(Keys.ENTER)
time.sleep(4)

expected_text=driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text

assert expected_text == '"Videojuegos"'


time.sleep(4)

driver.close()

# this is a comment for understanding git
# this is a comment for the branch1