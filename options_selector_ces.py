from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

service = Service(os.getenv('STORE_YOUR_PATH_TO_CHROME_DRIVER'))
driver = webdriver.Chrome(service=service)

driver.get("http://103.56.30.205/kitsw/")

# store your username and password in a .env file
load_dotenv()

uname = os.getenv('STORE_YOUR_USERNAME')
pswd = os.getenv('STORE_YOUR_USERPASSWORD')

text_for_text_box = 'punctuality' # change this to the option you want to type in the text box

driver.maximize_window()

## login
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR ,"input#uname"))
)

uname_element = driver.find_element(By.CSS_SELECTOR ,"input#uname")
uname_element.click()
uname_element.send_keys(uname)

# time.sleep(2)

pwd_element = driver.find_element(By.CSS_SELECTOR ,"input#pwd")
pwd_element.click()
pwd_element.send_keys(pswd + Keys.RETURN)


# time.sleep(5)

## next page to fill details
def options_clicker():
    WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CSS_SELECTOR ,"select#id1.form-control"))
    )

    total_elements = driver.find_elements(By.CLASS_NAME ,"form-control")
    total_elements = (len(total_elements) - 2)
    print(total_elements)

    # if the below for won't work then use the above code <: for bhanu
    # text_input = driver.find_element((By.CSS_SELECTOR ,"input#id5.form-control"))
    # text_input.click()
    # text_input.send_keys(text_for_text_box)

    for i in range(1, total_elements):
        # select_element = driver.find_element(By.CSS_SELECTOR ,"select#id" + str(i) + ".form-control")
        select_element = driver.find_element(By.CSS_SELECTOR , f"#id{i}.form-control")
        # time.sleep(1)

        # if input is text
        if i == 5:
            select_element.click()
            select_element.send_keys(text_for_text_box)

        if len(select_element.find_elements(By.CSS_SELECTOR, "option")) == 7:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 6)

        elif len(select_element.find_elements(By.CSS_SELECTOR, "option")) == 6:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 5)

        elif len(select_element.find_elements(By.CSS_SELECTOR, "option")) == 5:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 4)

        elif len(select_element.find_elements(By.CSS_SELECTOR, "option")) == 4:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 3)

        elif len(select_element.find_elements(By.CSS_SELECTOR, "option")) == 3:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 1)

        else:
            select_element.click()
            select_element.send_keys(Keys.DOWN * 4)


    submit_element = driver.find_element(By.CSS_SELECTOR , "input.btn-success")
    submit_element.click()

    time.sleep(10)

    # ok = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "ok")))
    ok = driver.find_element(By.PARTIAL_LINK_TEXT, "ok")
    ok.click()

#change the range value to the number of forms you want to fill
for i in range(6):
    try:
        options_clicker()
        time.sleep(5)
    except:
        print("if you this message, May be you have already filled the form. or there might be some other issue.")
        continue

driver.quit()