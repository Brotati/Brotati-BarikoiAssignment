import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.barikoi.com/search")

input_container = driver.find_element(By.CLASS_NAME, "input-container")
search_input = input_container.find_element(By.TAG_NAME, "input")

#search_input.send_keys("mirpur")
#search_input.send_keys("puran dhaka")
#search_input.send_keys("gulshan2")
#search_input.send_keys("nikunjo")
search_input.send_keys("american international university-bangladesh")

time.sleep(10)

search_result = driver.find_element(By.CLASS_NAME, "autocomplete-content")
search_result_list = search_result.find_elements(By.TAG_NAME, "li")
search_result_list[0].click()


while True:
    pass