import tkinter as tk
import time 

def relogio(): 
    data = time.strftime('%b %d, %y')
    horario = time.strftime('%H:%M:%S')

    label_data.config(text = data)
    label_relogio.config(text = horario)

    
    janela.after(1000, relogio)

janela = tk.Tk()
janela.title('Relogio Digital')
janela.configure(bg = "white")

label_data = tk.Label(janela, font = ("Calibri", 40), bg = "white", fg="cyan")
label_data.pack(padx= 0, pady= 1)
label_relogio = tk.Label(janela, font = ("Calibri", 80), bg = "white", fg="cyan")
label_relogio.pack(padx= 10, pady=10)

relogio()

janela.mainloop()