from selenium import webdriver
import time

name = "David Mai"
email = "maidavidx@gmail.com"
tel = "2535333967"
address = "123 somewhere"
zip = "98105"
city = "Seattle"

number = "1111 1111 1111 1111"
expiration_month = "10"
expiration_year = "2023"
cvv = "123"

chromedriver_location = "chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click

time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath =
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_xpath =
driver.find_element_by_xpath(email_xpath).send_keys(email)

tel_xpath =
driver.find_element_by_xpath(tel_xpath).send_keys(tel)

address_xpath =
driver.find_element_by_xpath(address_xpath).send_keys(address)

zip_xpath =
driver.find_element_by_xpath(zip_xpath).send_keys(zip)

city_xpath =
driver.find_element_by_xpath(city_xpath).send_keys(city)

state_xpath = '//*[@id="order_billing_state/option[56]'
driver.find_element_by_xpath(state).click()

numbers_xpath =
driver.find_element_by_xpath(numbers_xpath).send_keys(numbers)

card_month_xpath =
driver.find_element_by_xpath(card_month_xpath).click()

cvv_xpath =
driver.find_element_by_xpath(cvv_xpath).send_keys(cvv)

agree_xpath =
driver.find_element_by_xpath(agree_xpath).click()

process_payment_xpath =
driver.find_element_by_xpath(process_payment_xpath).click()


print("Web Driver Run")