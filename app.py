import webbrowser
import pyautogui as gui
from time import sleep 


def deslogar():
    gui.click(x=-220,y=789, duration=2)
    gui.click(x=-1594,y=1069, duration=2)
    gui.click(x=-1576,y=991, duration=2)
    gui.hotkey('Ctrl', 'w')


# Navegar até o site e pegar os dados de login
while True:
    usuario_instagram = gui.prompt(text='Digite o telefone, email ou nome de usuário: ', title='Dados do usuário')
    senha = gui.password(text='Digite a senha: ', title='Dados do usuário', mask='*')

    webbrowser.open('https://instagram.com') 
    sleep(5)

    # Clicar em usuário e digitar

    gui.click(x=-652,y=577,duration=2)
    gui.typewrite(usuario_instagram)

    # Clicar em senha e digitar senha

    gui.press('tab')
    sleep(1)
    gui.typewrite(senha)

    # Clicar em entrar

    gui.press('tab', presses=2)
    sleep(1)
    gui.press('enter')
    sleep(5)

    # Clicar em 'Agora não' para não salvar informações

    gui.click(x=-707,y=782, duration=2)
    sleep(3)

    # Clicar em pesquisa e digitar qual página que deseja curtir as fotos

    gui.click(x=-1589,y=559, duration=2)
    gui.typewrite('Nike')
    sleep(2)

    # Clicar na página que deseja

    gui.click(x=-1444,y=545, duration=2)
    sleep(3)

    # Clicar sempre na primeira (ultimo post) foto.

    gui.click(x=-1101,y=1067, duration=4)
    sleep(5)

    # Se tiver curtida: pausar o bot por 24hrs. Se não tiver curtida, curtir e comentar a foto

    like = gui.locateCenterOnScreen('coracao.PNG')
    if like is not None:
        sleep(86400)
        deslogar()
    elif like == None:
        gui.click(x=-929,y=930,duration=2)
        gui.click(x=-820,y=1066,duration=3)
        gui.typewrite('Bela foto!')
        sleep(2)
        gui.press('enter')
        deslogar()

    # Pausar por 24hrs
        sleep(86400)