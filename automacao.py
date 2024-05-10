import pyautogui as pay
import time


#pay.PAUSE(3.0)

pay.press("win")
pay.write("chrome")
pay.press("enter")
time.sleep(5)


pay.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pay.press("enter")
time.sleep(3)
pay.click(x=727, y=411)
time.sleep(3)

pay.write("yasmin@gmail.com")
pay.press("tab")
pay.write("0123")
pay.press("tab")
pay.press("enter")
time.sleep(3)

import pandas as pd

tabela = pd.read_csv('produtos.csv')

pay.click(x=773, y=296)

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])

    pay.click(x=773, y=296)

    pay.write(str(tabela.loc[linha, "codigo"]))
    pay.press("tab")

    pay.write(str(tabela.loc[linha, "marca"]))
    pay.press("tab")

    pay.write(str(tabela.loc[linha, "tipo"]))
    pay.press("tab")

    pay.write(str(tabela.loc[linha, "categoria"]))
    pay.press("tab") 

    pay.write(str(tabela.loc[linha, "preco_unitario"]))
    pay.press("tab")

    pay.write(str(tabela.loc[linha, "custo"]))
    pay.press("tab")

    obs = pay.write(str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pay.write(obs)

    pay.press("tab")

    pay.press("enter")

    pay.press("pageup")