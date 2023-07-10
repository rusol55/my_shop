# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# reg_mail = driver.find_element(By.ID,"reg_email")
# reg_mail.send_keys("rusol55@gmail.com")
# reg_password = driver.find_element(By.ID,"reg_password")
# reg_password.send_keys("Opc100218!")
# register = driver.find_element(By.XPATH,'''//*[@id="customer_login"]/div[2]/form/p[3]/input[3]''')
# register.click()
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
my_acc.click()
log_mail = driver.find_element(By.ID,"username")
log_mail.send_keys("rusol55@gmail.com")
log_password = driver.find_element(By.ID,"password")
log_password.send_keys("Opc100218!")
login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
login.click()
logout = driver.find_element(By.LINK_TEXT,"Logout")
logout_get_text = logout.text
assert logout_get_text == "Logout"