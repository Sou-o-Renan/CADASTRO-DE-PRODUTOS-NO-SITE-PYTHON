# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar Dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de Cadastro

import pyautogui
import time


pyautogui.PAUSE = 1

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 teclado do teclado
#pyautogui.hotkey -> combinação de teclas


# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

# entrando no site (navegador aberto)
time.sleep(5)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa (segundos)
time.sleep(5)

# fazer o login (click e digitar)
pyautogui.click(x=592, y=371) 
pyautogui.write("teste@gmail.com")
# fazer o login (passar para senha e digitar senha)
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.click(x=678, y=526)
time.sleep(3)

# importando a base de dados
# pip install pandas e pip install pandas numpy openyxl (no cmd)
import pandas
tabela = pandas.read_csv("produtos.csv") # variavel e tipo do arquivo 

# cadastrar um produto

for linha in tabela.index:
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=561, y=251)
    pyautogui.write(codigo) 
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) 
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) 
    pyautogui.press("tab")

    #preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario) 
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) 
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs) 
    
    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")    
    pyautogui.scroll(5000)









