import webbrowser
import pyautogui as gui
from time import sleep 




# Navegar até o site e pegar os dados de login

email = gui.prompt(text='Digite o telefone, email ou nome de usuário: ', title='Dados do usuário')
senha = gui.password(text='Digite a senha: ', title='Dados do usuário',mask='*')

webbrowser.open('https://instagram.com') 
sleep(5)

# Clicar em usuário e digitar

gui.click(x=-652,y=577,duration=2)
gui.typewrite(email)

# Clicar em senha e digitar senha

gui.press('tab')
sleep(1)
gui.typewrite(senha)

# Clicar em entrar

gui.press('tab', presses=2)
sleep(1)
gui.press('enter')

# Clicar em 'Nunca' para não salvar
# Clicar em 'Agora não' para não salvar informações
# Clicar em pesquisa e digitar qual página que deseja curtir as fotos
# Clicar na pagina que deseja
# Clicar sempre na primeira (ultimo post) foto.
# Se tiver curtida: pausar o bot por 24hrs
# Se não tiver curtida, curtir e comentar a foto
# Pausar por 24hrs
