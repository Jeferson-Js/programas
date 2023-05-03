from tkinter import *

window = Tk()
window.title('Primeiro app')
window.geometry("300x200+200+200")
window.iconbitmap('img/python.ico')
window.resizable(True, True)
window['bg'] = 'blue'
window.maxsize(700, 300)
window.minsize(500,200)
window = mainloop()