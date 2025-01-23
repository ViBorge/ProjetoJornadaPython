
    #Para importa a biblioteca, vai no terminal e use o código: pip install pyautogui
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

    #pyautogui.press() -> pressionar uma tecla
    #pyautogui.click() -> clicar
    #pyautogui.write() -> Escrever na aba

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.hotkey("ctrl" , "shift", "n")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)
pyautogui.click(x=738, y=373)
pyautogui.write("vini@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")


tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:

    pyautogui.click(x=738, y=258)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")



    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(100)


time.sleep(5)
pyautogui.hotkey("alt" , "F4")
