import PySimpleGUI as sg 

sg.change_look_and_feel('Python')

layout = [
    [sg.Text('Mensagem', size=(10,0)), sg.Input('', size=(15,0))],
    [sg.Output(size=(10,6))]
    [sg.Button('Entrar', size=(10,0)), sg.Button('Sair', size=(10,0))],
]

window = sg.Window('Hello World', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
window.close()