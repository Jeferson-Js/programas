from tkinter import *

window = Tk()
window.title('Aplicação')
window.geometry('400x300')
window['bg'] = 'purple'
btn = Button(window, text='Executar')
btn.pack(side='top', anchor='center')

# Obtém a largura e altura da tela
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Define a largura e altura da janela
width = 400
height = 300

# Calcula a posição x e y da janela para ficar no centro da tela
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# Define a posição e tamanho da janela
window.geometry(f'{width}x{height}+{x}+{y}')

window = mainloop()