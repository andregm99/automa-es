from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#abrindo navegador
navegador = webdriver.Chrome()


# Acessar o site 
navegador.get('https://ri.magazineluiza.com.br/ShowCanal/Planilha-de-Resultado?=CHN0/Z4bUSgrS8IkQeL+Wg==&linguagem=pt')

# Localiza e clica no botão de "Aceitar cookies" (no site da magazine luiza)
accept_button = navegador.find_element(By.XPATH, '//*[@id="6BKAw9gH52TSXKs4jdvWkw=="]')  # XPath correto
cookie= navegador.find_element(By.LINK_TEXT, 'OK')
cookie.click()
accept_button.click()

# Atraso para garantir que a ação seja realizada
time.sleep(5)
# Fechar o navegador
navegador.quit()
