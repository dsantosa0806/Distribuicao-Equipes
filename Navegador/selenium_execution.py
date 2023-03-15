import sys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


## Oh Lord, forgive me for what i'm about to Code !

equipe_1 = 'Equipe Cobrança 1 (Adina Ferreira Silva)'
equipe_2 = 'Equipe Cobrança 2 (Adriele Cerilo Mendes Monte)'
equipe_3 = 'Equipe Cobrança 3 (Anna Gontijo)'
equipe_4 = 'Equipe Cobrança 4 (Edney Bandeira Carvalho)'
equipe_5 = 'Equipe Cobrança 5 (Nathalia Ferreira Massad)'
equipe_6 = 'Equipe Cobrança 6 (Jéssica Vieira Lopes)'
equipe_7 = 'Equipe Cobrança 7 (Gabriel Kalil Moraes)'
equipe_8 = 'Equipe Cobrança 8 (Thiago Gamboa Vilar Martins)'
equipe_teste = 'Equipe Teste (Daniel)'


## Equipes Painel Paths
qtd_painel_1 = '//*[@id="gridDistribuicao"]/table/tbody/tr[1]/td[3]'
qtd_painel_2 = '//*[@id="gridDistribuicao"]/table/tbody/tr[2]/td[3]'
qtd_painel_3 = '//*[@id="gridDistribuicao"]/table/tbody/tr[3]/td[3]'
qtd_painel_4 = '//*[@id="gridDistribuicao"]/table/tbody/tr[4]/td[3]'
qtd_painel_5 = '//*[@id="gridDistribuicao"]/table/tbody/tr[5]/td[3]'
qtd_painel_6 = '//*[@id="gridDistribuicao"]/table/tbody/tr[6]/td[3]'
qtd_painel_7 = '//*[@id="gridDistribuicao"]/table/tbody/tr[7]/td[3]'
qtd_painel_8 = '//*[@id="gridDistribuicao"]/table/tbody/tr[8]/td[3]'

## Equipes Quantidade Paths

qtd_qtde_1 = '//*[@id="gridDistribuicao"]/table/tbody/tr[1]/td[4]'
qtd_qtde_2 = '//*[@id="gridDistribuicao"]/table/tbody/tr[2]/td[4]'
qtd_qtde_3 = '//*[@id="gridDistribuicao"]/table/tbody/tr[3]/td[4]'
qtd_qtde_4 = '//*[@id="gridDistribuicao"]/table/tbody/tr[4]/td[4]'
qtd_qtde_5 = '//*[@id="gridDistribuicao"]/table/tbody/tr[5]/td[4]'
qtd_qtde_6 = '//*[@id="gridDistribuicao"]/table/tbody/tr[6]/td[4]'
qtd_qtde_7 = '//*[@id="gridDistribuicao"]/table/tbody/tr[7]/td[4]'
qtd_qtde_8 = '//*[@id="gridDistribuicao"]/table/tbody/tr[8]/td[4]'

#Campos Form
input_devedor = '//*[@id="Devedor"]'
btn_consultar = '//*[@id="placeholder"]/div[1]/div/div[1]/button'
btn_distribuir = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr/td[10]/button'
quant_autos = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr/td[7]'
valor_total = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr/td[8]'
btn_distribuir_equipe = '//*[@id="btnDistribuir"]'
btn_cancelar = '/html/body/div[8]/div[2]/div[1]/div/div/button[2]'
btn_confirmar_analise = '/html/body/div[8]/div[2]/div[1]/div/div/button[1]'
txt_devedor = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr/td[6]'
btn_reverter = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr/td[10]/button'
txt_final_loop = '//*[@id="gridAnaliseCondicaoDevedor"]/div[1]'


def acessa_sior(navegador):
    try:
        #Acesso a tela de login
        url_login = 'http://servicos.dnit.gov.br/sior/Account/Login/?ReturnUrl=%2Fsior%2F'
        navegador.get(url_login)
    except:
        print('Erro', 'O SIOR apresentou instabilidade, '
                      'por favor reinicie a aplicação e tente novamente T:acessa_sior ')
        sys.exit()


def login(navegador,usuario,senha):
    username = usuario
    userpass = senha
    cpfpath = '// *[ @ id = "UserName"]'
    senhapath = '//*[@id="Password"]'
    clickpath = '//*[@id="FormLogin"]/div[4]/div[2]/button'
    err = True
    while err:
        try:
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, cpfpath))).send_keys(username)
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, senhapath))).send_keys(userpass)
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, clickpath))).click()

            time.sleep(2)

            err = False

        except:
            print('Erro', 'O SIOR apresentou instabilidade, '
                          'por favor reinicie a aplicação e tente novamente T:Login')
            sys.exit()


def acessa_tela_incial_distribuicao(navegador):
    # Acessa a tela da notificação da autuação
    url_base = 'https://servicos.dnit.gov.br/sior/Cobranca/EquipeDistribuicao'
    try:
        navegador.get(url_base)
    except:
        print('Erro', 'O SIOR apresentou instabilidade, '
                      'por favor reinicie a aplicação e tente novamente T:acessa_tela_incial_auto')
        sys.exit()


def analisa(navegador, devedor, quantidade):
    # Input devedor
    try:
        WebDriverWait(navegador, 50).until(
            EC.element_to_be_clickable((By.XPATH, input_devedor))).send_keys(devedor)
    except:
        print(f'Erro {devedor}', 'Input devedor')
        return 1

    # Clique BTN Consultar
    try:
        WebDriverWait(navegador, 40).until(
            EC.element_to_be_clickable((By.XPATH, btn_consultar))).click()

        err = True
        while err:
            time.sleep(1)
            text = WebDriverWait(navegador, 40).until(
                EC.presence_of_element_located((By.XPATH, txt_devedor))).text
            if devedor in text:
                err = False
            else:
                err = True

    except:
        print(f'Erro {devedor}', 'Btn Consultar')
        return 1

    # Aqui deve-se analisar a Quantidade e o Piso
    try:
        qtde = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, quant_autos))).text
        valor = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, valor_total))).text
        if int(qtde) != quantidade:
            print(f'Erro {devedor}', 'A quantidade do SIOR é diferente da quantidade liberada')
            return 1
        elif float(valor.replace('.','').replace(',','.')) < 800.0:
            print(f'Erro {devedor}', 'Valor total abaixo do piso')
            return 1
    except:
        print(f'Erro {devedor}', 'Analise de Quantidade e Valor')
        return 1

    # Clique BTN Distribuir
    try:
        botao_distribuir = WebDriverWait(navegador, 40).until(
            EC.element_to_be_clickable((By.XPATH, btn_distribuir))).text
        if botao_distribuir == 'Distribuir':
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir))).click()
        else:
            print(f'---------------------------------------------------------------------------------\n')
            print(f'Devedor já distribudo {devedor}\n')
            return 3
    except:
        print(f'Erro {devedor}', 'Btn Distribuir')
        return 1

    # Inicio do Bloco de Distribuição Equipe 1
    try:
        qtde_1 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_1))).text
        if int(qtde_1) <= 150:
            quantidade_input = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_1)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input)
            actions.send_keys(' ',quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)

            print(f'{equipe_1} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 2
    try:
        qtde_2 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_2))).text
        if int(qtde_2) <= 168:
            quantidade_input_2 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_2)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_2)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_2} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 3
    try:
        qtde_3 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_3))).text
        if int(qtde_3) <= 180:
            quantidade_input_3 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_3)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_3)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_3} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 4
    try:
        qtde_4 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_4))).text
        if int(qtde_4) <= 168:
            quantidade_input_4 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_4)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_4)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_4} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 5
    try:
        qtde_5 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_5))).text
        if int(qtde_5) <= 168:
            quantidade_input_5 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_5)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_5)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_5} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 6
    try:
        qtde_6 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_6))).text
        if int(qtde_6) <= 168:
            quantidade_input_6 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_6)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_6)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_6} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 7
    try:
        qtde_7 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_7))).text
        if int(qtde_7) <= 168:
            quantidade_input_7 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_7)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_7)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_7} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            pass
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1

    # Inicio do Bloco de Distribuição Equipe 8
    try:
        qtde_8 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_8))).text
        if int(qtde_8) <= 151:
            quantidade_input_8 = WebDriverWait(navegador, 50).until(
                EC.presence_of_element_located((By.XPATH, qtd_qtde_8)))
            actions = ActionChains(navegador)
            actions.click(quantidade_input_8)
            actions.send_keys(' ', quantidade)
            actions.perform()
            # Distribui a equipe
            WebDriverWait(navegador, 40).until(
                EC.element_to_be_clickable((By.XPATH, btn_distribuir_equipe))).click()

            # Clique Busca texto Reverter
            err = True
            while err:
                time.sleep(1)
                reverter = WebDriverWait(navegador, 120).until(
                    EC.presence_of_element_located((By.XPATH, btn_reverter))).text
                if reverter == 'Reverter':
                    err = False
                    time.sleep(1)
                else:
                    err = True
                    time.sleep(1)
            print(f'{equipe_8} Distribuído - {quantidade} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return 1
        else:
            return 2
    except:
        print(f'Erro {devedor} Não distribuído')
        return 1


# Bloco Final
def extracao_final(navegador):
    # Input devedor
    btn = '//*[@id="gridEquipeDistribuicao"]/table/tbody/tr[1]/td[10]/button'

    # Clique BTN Distribuir
    try:
        WebDriverWait(navegador, 40).until(
            EC.element_to_be_clickable((By.XPATH, btn_consultar))).click()
    except:
        print('Erro Extração Final')

    try:
        WebDriverWait(navegador, 40).until(
            EC.element_to_be_clickable((By.XPATH, btn))).click()
    except:
        print('Erro Extração Final')

    try:
        qtde_1 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_1))).text
        qtde_2 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_2))).text
        qtde_3 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_3))).text
        qtde_4 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_4))).text
        qtde_5 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_5))).text
        qtde_6 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_6))).text
        qtde_7 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_7))).text
        qtde_8 = WebDriverWait(navegador, 40).until(
            EC.presence_of_element_located((By.XPATH, qtd_painel_8))).text
        print(
            f'BLOCO DE DISTRIBUIÇÃO {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
            f'---------------------------------------------------------------------------------\n'
            f'{equipe_1} - {qtde_1} \n'
            f'{equipe_2} - {qtde_2} \n'
            f'{equipe_3} - {qtde_3} \n'
            f'{equipe_4} - {qtde_4} \n'
            f'{equipe_5} - {qtde_5} \n'
            f'{equipe_6} - {qtde_6} \n'
            f'{equipe_7} - {qtde_7} \n'
            f'{equipe_8} - {qtde_8} \n'
            f'---------------------------------------------------------------------------------\n'
        )
    except:
        print('Erro Extração Final')
