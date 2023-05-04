import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        #Tela
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar dados')]
        ]

        window = sg.Window('Informações do usuário').layout(layout)

        self.button, self.values = window.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()