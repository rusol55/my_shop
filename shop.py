# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# log_mail = driver.find_element(By.ID,"username")
# log_mail.send_keys("rusol55@gmail.com")
# log_password = driver.find_element(By.ID,"password")
# log_password.send_keys("Opc100218!")
# login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.ID,"menu-item-40")
# shop.click()
# html5 = driver.find_element(By.CSS_SELECTOR,"img[title='Mastering HTML5 Forms']")
# html5.click()
# head = driver.find_element(By.CSS_SELECTOR,"#product-181 > div.summary.entry-summary > h1")
# head_get_text = head.text
# assert head_get_text == "HTML5 Forms"
# 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# log_mail = driver.find_element(By.ID,"username")
# log_mail.send_keys("rusol55@gmail.com")
# log_password = driver.find_element(By.ID,"password")
# log_password.send_keys("Opc100218!")
# login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.ID,"menu-item-40")
# shop.click()
# html_3 = driver.find_element(By.CSS_SELECTOR,"#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
# html_3.click()
# col = driver.find_element(By.XPATH,'''//*[@id="woocommerce_product_categories-2"]/ul/li[2]/span''')
# col_get_text = col.text
# assert col_get_text == "(3)"
import time

# 3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# log_mail = driver.find_element(By.ID,"username")
# log_mail.send_keys("rusol55@gmail.com")
# log_password = driver.find_element(By.ID,"password")
# log_password.send_keys("Opc100218!")
# login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.ID,"menu-item-40")
# shop.click()
# selector = driver.find_element(By.CSS_SELECTOR,"#content > form > select > option:nth-child(1)")
# selector_value = selector.get_attribute("value")
# assert selector_value == "menu_order"
# element = driver.find_element(By.CLASS_NAME,"orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# element_sel = driver.find_element(By.CLASS_NAME,"orderby")
# element_sel_value = element_sel.get_attribute("value")
# assert element_sel_value == "price-desc"


# 4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# log_mail = driver.find_element(By.ID,"username")
# log_mail.send_keys("rusol55@gmail.com")
# log_password = driver.find_element(By.ID,"password")
# log_password.send_keys("Opc100218!")
# login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.ID,"menu-item-40")
# shop.click()
# andr = driver.find_element(By.CSS_SELECTOR,".post-169 h3")
# andr.click()
# book_old_price = driver.find_element(By.CSS_SELECTOR,".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element(By.CSS_SELECTOR,".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cower = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "images")))
# book_cower.click()
# book_cower_close = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# book_cower_close.click()

# 5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_acc = driver.find_element(By.CSS_SELECTOR,"#menu-item-50 > a")
# my_acc.click()
# log_mail = driver.find_element(By.ID,"username")
# log_mail.send_keys("rusol55@gmail.com")
# log_password = driver.find_element(By.ID,"password")
# log_password.send_keys("Opc100218!")
# login = driver.find_element(By.CSS_SELECTOR,"p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.ID,"menu-item-40")
# shop.click()
# basket = driver.find_element(By.XPATH,'''//*[@id="content"]/ul/li[4]/a[2]''')
# basket.click()
# time.sleep(10)
# col = driver.find_element(By.CSS_SELECTOR,"a > span.cartcontents")
# col_text = col.text
# assert "1" in col_text
# price = driver.find_element(By.CSS_SELECTOR, "a > span.amount")
# price_text = price.text
# assert price_text == "₹180.00"
# basket_all = driver.find_element(By.ID,"wpmenucartli")
# basket_all.click()
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "180.00"))
# total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total > td > strong > span"), "183.60"))

# 6
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element(By.CSS_SELECTOR,"#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# basket = driver.find_element(By.XPATH,'''//*[@id="content"]/ul/li[4]/a[2]''')
# basket.click()
# time.sleep(15)
# basket2 = driver.find_element(By.XPATH,'''//*[@id="content"]/ul/li[5]/a[2]''')
# basket2.click()
# basket_all = driver.find_element(By.ID,"wpmenucartli")
# time.sleep(10)
# basket_all.click()
# time.sleep(5)
# close1 = driver.find_element(By.XPATH,'''//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a''')
# close1.click()
# time.sleep(10)
# undo = driver.find_element(By.LINK_TEXT,"Undo?")
# undo.click()
# quantity = driver.find_element(By.CSS_SELECTOR," tr:nth-child(2) > td.product-quantity > div > input")
# quantity.clear()
# quantity.send_keys(3)
# updete = driver.find_element(By.CSS_SELECTOR," tr:nth-child(3) > td > input.button")
# updete.click()
# element = driver.find_element(By.CSS_SELECTOR," tr:nth-child(2) > td.product-quantity > div > input")
# element_check = element.get_attribute("value")
# assert element_check == "3"
# time.sleep(15)
# coupon = driver.find_element(By.CSS_SELECTOR," tr:nth-child(3) > td > div > input.button")
# coupon.click()
# please = driver.find_element(By.CSS_SELECTOR,"div.woocommerce > ul > li")
# please_text = please.text
# assert please_text =="Please enter a coupon code."

# 7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element(By.CSS_SELECTOR,"#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
basket = driver.find_element(By.XPATH,'''//*[@id="content"]/ul/li[4]/a[2]''')
basket.click()
time.sleep(15)
basket_all = driver.find_element(By.ID,"wpmenucartli")
basket_all.click()
checkout = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".wc-proceed-to-checkout > a")))
checkout.click()
fist_name = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
fist_name.send_keys("ruslan")
last_name = driver.find_element(By.ID,"billing_last_name")
last_name.send_keys("solodovnikov")
mail = driver.find_element(By.ID,"billing_email")
mail.send_keys("rusol55@gmail.com")
phone = driver.find_element(By.ID,"billing_phone")
phone.send_keys("+71231231212")
selector = driver.find_element(By.CLASS_NAME,"select2-arrow")
selector.click()
time.sleep(5)
country = driver.find_element(By.ID,"s2id_autogen1_search")
country.send_keys("Qatar")
time.sleep(10)
count = driver.find_element(By.CSS_SELECTOR,"span.select2-match")
count.click()
adress = driver.find_element(By.ID,"billing_address_1")
adress.send_keys("piter")
city = driver.find_element(By.ID,"billing_city")
city.send_keys("spb")
state = driver.find_element(By.XPATH,'''//*[@id="billing_state"]''')
state.send_keys("russia")
time.sleep(10)
postcode = driver.find_element(By.ID,"billing_postcode")
postcode.send_keys("22")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
option = driver.find_element(By.ID,"payment_method_cheque")
option.click()
time.sleep(10)
order = driver.find_element(By.ID,"place_order")
order.click()
thank = driver.find_element(By.CSS_SELECTOR," p.woocommerce-thankyou-order-received")
thank_text = thank.text
assert thank_text == "Thank you. Your order has been received."
method = driver.find_element(By.CSS_SELECTOR,"tr:nth-child(3) > td")
method_text = method.text
assert method_text == "Check Payments"





