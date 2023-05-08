import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        sg.theme('Python')
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(19,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(19,0), key='idade')],
            [sg.Text('Quais provedores de emails são aceitos?')],
            [sg.Checkbox('Gmail', key='gamil'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahool', key='yahool')],
            [sg.Button('Enviar dados', size=(15,0))],
            [sg.Output(size=(35, 5))]
        ]

        self.window = sg.Window('Informações do usuário').layout(layout)


    def Iniciar(self):
        while True:
            self.button, self.values = self.window.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gamil = self.values['gamil']
            aceita_outlook = self.values['outlook']
            aceita_yahool = self.values['yahool']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita gmail: {aceita_gamil}')
            print(f'Aceita outlook: {aceita_outlook}')
            print(f'Aceita yahool: {aceita_yahool}')


tela = TelaPython()
tela.Iniciar()