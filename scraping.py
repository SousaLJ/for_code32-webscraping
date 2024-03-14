from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json, os

options = Options()
options.page_load_strategy = 'none'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

driver.get('https://www.glassdoor.com.br')

def save_cookies(driver):
    #get cookies from session 
    #Use it after login to save the coockies
    coockies = driver.get_cookies()

    #Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(coockies, file)
    print('Cookies salvos com sucesso!')

def login(driver):
    email = ""
    senha = ""
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/section[1]/div[2]/div/div/div[1]/div/div/div/div/form/div[1]/div/div[1]/input"))
        )
        print("elemento carregou")
    except:
        print("Elemento não carregou")

    email_field = driver.find_element(By.XPATH, "/html/body/div[2]/section[1]/div[2]/div/div/div[1]/div/div/div/div/form/div[1]/div/div[1]/input")
    sleep(3)
    email_field.send_keys(email)

    email_login_button = driver.find_element(By.XPATH, "/html/body/div[2]/section[1]/div[2]/div/div/div[1]/div/div/div/div/form/div[2]/button")
    email_login_button.click()
    sleep(3)

    password_field = driver.find_element(By.XPATH, "/html/body/div[2]/section[1]/div[2]/div/div/div[1]/div/div/div/div/form/div[1]/div[1]/div/div[1]/input")
    password_field.send_keys(senha)

    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/section[1]/div[2]/div/div/div[1]/div/div/div/div/form/div[2]/button")
    login_button.click()


    save_cookies(driver)

"""def load_cookies():
    if 'cookies.json' in os.listdir():
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()        
    else:
        login(driver=driver)
"""
if __name__ == "__main__":
    login(driver=driver)