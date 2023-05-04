import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario_correto = 'Jeferson'
        senha_correta = '123456'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Usuário logado com sucesso!')
        else:
            window['mensagem'].update('Usuário ou senha incorretos!')