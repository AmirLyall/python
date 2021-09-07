# -*- coding: utf-8 -*-
"""
Spyder Editor

Bot to purchase something from from Best Buy

Assumptions:
    1 - using chrome in incognito mode
    2 - shipping to home
    3 - no credit card info saved in the account
"""

# import selenium packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64

# insert your base64 password here - this goes on line 78. Alternatively, enter it directly.
password_key = base64.b64decode("<PASSWORD>").decode("utf-8")

successful = False #initialized in memory without a value
while successful == False:

    try:
        # open Chrome, navigate to URL
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome("<PATH_TO>/chromedriver_win32/chromedriver.exe", options=chrome_options)
        driver.get("https://www.bestbuy.com/site/net10-keep-your-own-phone-sim-card-kit/5470401.p?skuId=5470401")
    
    except Exception:
        driver.close()
        # driver.delete_all_cookies()
    
    try:
        # add product to cart
        wait = WebDriverWait(driver, 5)
        # email_address = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')))
        # add_to_cart = driver.find_element_by_xpath("//button[contains(text(),'Add to Cart')]")
        add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div[3]/div[5]/div[1]/div/div/div/button')))
        add_to_cart.click()
           
    except Exception:
        driver.close()
    
    try:
        # navigate to cart, click ship to home, click checkout
        driver.get("https://www.bestbuy.com/cart")
        wait = WebDriverWait(driver, 5)
        shipping = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input')))
        shipping.click()  

        checkout = driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')
        checkout.click()

    except Exception:
        driver.close()
    
    try:
        # enter email address and password
        wait = WebDriverWait(driver, 5)
        email_address = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')))
        email_address.clear()
        email_address.send_keys("<EMAIL ADDRESS>")
    
    except Exception:
        driver.close()
    
    try:
        wait = WebDriverWait(driver, 5)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[2]/div/input')))
        password.clear()
        password.send_keys(password_key)
        sign_in = driver.find_element_by_xpath("//button[contains(text(),'Sign In')]")
        sign_in.click()
    
    except Exception:
        driver.close()
        
    try:
        wait = WebDriverWait(driver, 5)
        
        first_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input')))
        first_name.clear()
        first_name.send_keys("<FIRST NAME>")
        
        last_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input')))
        last_name.clear()
        last_name.send_keys("<LAST NAME>")
        
        address = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input')))
        address.clear()
        address.send_keys("<ADDRESS>")
        
        city = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input')))
        city.clear()
        city.send_keys("<CITY>")
        
        state = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[2]/label/div/div/select/option[text()='NC']").click()
        
        zip_code = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input')))
        zip_code.clear()
        zip_code.send_keys("<ZIP>")
        
        phone_number = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input')))
        phone_number.clear()
        phone_number.send_keys("<PHONE NUMBER>")
        
        # payment_information = driver.find_element_by_xpath("//button[contains(text(),'Continue to Payment Information')]")
        payment_information = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span')))
        payment_information.click()

    except Exception:
        driver.close()
        
    try:
        wait = WebDriverWait(driver, 5)
        
        cc_num = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input')))
        cc_num.clear()
        cc_num.send_keys("<CREDIT CARD NUMBER>")
        
        #edit your mm/yyyy information for the dropdown
        exp_mm = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select/option[text()='05']").click()
        
        exp_yyyy = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select/option[text()='2022']").click()
        
        security_code = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input')))
        security_code.clear()
        security_code.send_keys("<SECURITY CODE>")

        # payment_information = driver.find_element_by_xpath("//button[contains(text(),'Continue to Payment Information')]")
        place_order = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button')))
        place_order.click()
        
    except Exception:
        driver.close()
    
    successful=True
