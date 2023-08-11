import pandas as pd
import urllib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from save import chrome_driver_path, chrome_save_path

df = pd.read_excel("../planilhas/clientes_filtrados.xlsx")

def carregar(browser: webdriver):
    while len((browser.find_elements(By.ID, 'side'))) < 1:
        sleep(1)
    return

def enviar(browser: webdriver, cliente):
    wait = WebDriverWait(browser, 9)
    try:        
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
        # element.click()
        
        print(f"Mensagem enviada para {cliente} com sucesso")
        sleep(2)
        return True
    
    except Exception as error:
        print(f"Nao foi possível enviar mensagem para {cliente}")
        if len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) >= 1:
            print("Número inválido")
        else:
            print(error, type(error).__name__)
        return False

#Configurando e abrindo o chrome
options = webdriver.ChromeOptions()
options.add_argument(chrome_save_path)
browser = webdriver.Chrome(options=options)

browser.get("http://web.whatsapp.com") #Acessando whatsapp

carregar(browser=browser)

sucss, fail = 0, 0

for i, n in enumerate(df["Nome"]):
    nome = n.split()[0].title()
    mensagem = urllib.parse.quote(f"""
Olá, {nome}, aqui é da CrbFinanceira, nosso sistema detectou que você possui parcelas em atrado conosco. Não se preocupe, podemos resolver isso para você, apenas entre em contato conosco!
""")

    numero = df.loc[i, "Telefone"]
    link = f"http://web.whatsapp.com/send?phone=55{numero}&text={mensagem}"
    browser.get(link)
    if enviar(browser=browser, cliente=nome):
        sucss += 1
    else:
        fail += 1
        df.drop(index=i, inplace=True)

print(f"Sucessos: {sucss}")
print(f"Falhas: {fail}")

df.to_excel("../planilhas/clientes_filtrados.xlsx", index=False)
