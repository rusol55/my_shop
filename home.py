import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element(By.CSS_SELECTOR,"#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
selenium_ruby.click()
rewiews = driver.find_element(By.CLASS_NAME,"reviews_tab")
rewiews.click()
stars = driver.find_element(By.CLASS_NAME,"star-5")
stars.click()
rewiew = driver.find_element(By.ID,"comment")
rewiew.send_keys("Nice book!")
author = driver.find_element(By.ID,"author")
author.send_keys("rusol55")
mail = driver.find_element(By.ID,"email")
mail.send_keys("rusol55@gmail.com")
submit = driver.find_element(By.ID,"submit")
submit.click()
driver.quit()