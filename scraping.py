from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from model import Vagas

options = Options()
options.page_load_strategy = 'none'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

def login(driver):
    

    
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



def get_vagas():
    driver.get('https://www.glassdoor.com.br')

    login(driver)

    sleep(5)
    search_field = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/form/div[2]/div[1]/div/input")
    search_field.send_keys("estágio em engenharia química")
    local = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/form/div[2]/div[2]/div/input")
    local.send_keys("Rio de Janeiro")
    search_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div[2]/span"))
        )
        btn_close = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/span")
        btn_close.click()
    except:
        print("modal não carregou")

    elements = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardWrapper__lyvNS")

    lista_vagas = []

    for element in elements:
        element.click()

        title = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/header/div[1]/h1")

        #to_do: Falta capturar as informações a baixo
        description = ""

        company = ""

        link = ""

        vaga = Vagas.Vagas(title.text, description, company, link)
        lista_vagas.append(vaga)
        sleep(2)

    return lista_vagas
    