from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do navegador
navegador = webdriver.Chrome()

# Acessa o site
navegador.get('https://www.hashtagtreinamentos.com/')

#maximiza o navegador
navegador.maximize_window()

# Espera até o botão de fechar aparecer no pop-up
botao_fechar = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="botaoPopupFechar"]'))  # XPath do botão
)

# Clica no botão de fechar
botao_fechar.click()
print("Pop-up fechado com sucesso!")

# Aguarda alguns segundos para garantir que a ação foi realizada
time.sleep(5)

# Fecha o navegador
navegador.quit()
