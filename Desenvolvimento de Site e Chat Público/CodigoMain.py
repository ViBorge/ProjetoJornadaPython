## pip install flet

from queue import Full
import flet as ft





def main(pagina):

    #Eventos
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(linha_enviar)
        pagina.add(chat)
        nome = caixa_nome.value
        mensagem_tunel = f"{nome}: entrou no Chat"
        pagina.pubsub.send_all(mensagem_tunel)
        pagina.update()

    def enviar_mensagem(evento):
        nome = caixa_nome.value
        mensagem = campo_mensagem.value
        mensagem_tunel = f"{nome}: {mensagem}"
        pagina.pubsub.send_all(mensagem_tunel)
        
        campo_mensagem.value = ""
        pagina.update()

    def tunel_mensagem(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(tunel_mensagem)

    #Titulo
    titulo = ft.Text("ChatZap")
    pagina.add(titulo)

    #Popup
    titulo_popup = ft.Text("Bem vindo ao ChatZap")       #Printf
    caixa_nome = ft.TextField(label="Digite seu nome")   #Input
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    if caixa_nome.value != None:
        popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    
    #Botao
    botao = ft.ElevatedButton("Entrar no Chat", on_click=abrir_popup)
    pagina.add(botao)

    #Chat
    campo_mensagem = ft.TextField(label="Digite aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    chat = ft.Column()

    
#Define funçao main em tipo flet
ft.app(main, view=ft.WEB_BROWSER) #abri no gogle usar (main, view=ft.WEB_BROWSER), de para interrompe o codigo, ir no terminal e usar crtl + c

