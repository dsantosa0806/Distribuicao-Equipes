from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd
from Navegador.selenium_execution import acessa_sior, login, analisa, acessa_tela_incial_distribuicao, extracao_final


def option_navegador():

    options = webdriver.ChromeOptions()
    options.add_argument("enable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    return options


def service_navegador():
    serv = Service(ChromeDriverManager().install())
    return serv


navegador = webdriver.Chrome(options=option_navegador(),service=service_navegador())

acessa_sior(navegador)
# Passar aqui Login e Senha do SIOR
login(navegador,'','')
acessa_tela_incial_distribuicao(navegador)

table = pd.read_excel('tables/devedor_distribuir.xlsx')

# Atribuindo dados para variáveis
for i, devedor in enumerate(table['Devedor']):
    qtde_aits_prevista = int(table.loc[i,'Qtde'])

    retorno = analisa(navegador, devedor, qtde_aits_prevista)
    if retorno == 1:
        acessa_tela_incial_distribuicao(navegador)
        continue
    elif retorno == 2:
        break
    elif retorno == 3:
        acessa_tela_incial_distribuicao(navegador)
        continue
    # Finaliza o Loop
    acessa_tela_incial_distribuicao(navegador)

acessa_tela_incial_distribuicao(navegador)
extracao_final(navegador)

