import requests
from tkinter import *

def pegar_cotacoes():

    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    
    response = requisicao.json()

    cotacao_dolar = response['USDBRL']['bid']
    cotacao_euro = response['EURBRL']['bid']
    cotacao_btc = response['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    EURO: {cotacao_euro}
    BTC: {cotacao_btc}
    '''
    cotacao["text"] = texto



window = Tk()

window.title('Cotação do dia')

text_orientacao = Label(window, text='Click no botão para ver as cotações das moedas!')
text_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(window, text='Buscar cotações', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

cotacao = Label(window, text='')
cotacao.grid(column=0, row=2)

window.mainloop()