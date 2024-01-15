from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

cor0 = "#444466"
cor1 = "#feffff"
cor3 = "#f05a43"

janela = Tk()
janela.title("Gerador de senha")
janela.geometry("295x350")
janela.configure(bg=cor1)

frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief=FLAT)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor0, pady=0, padx=0, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

estilo = ttk.Style(janela)

img = Image.open("password.png")

img = img.resize((45,45), Image.Resampling.LANCZOS)

img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief=FLAT, anchor=NW, bg=cor1)
app_logo.place(x=2, y=0)

app_texto = Label(frame_cima, text="Gerador de senhas", height=60, padx=10, relief=FLAT,font=("Ivi 15 bold"), anchor=NW, bg=cor1, fg=cor0)
app_texto.place(x=60, y=10)





estilo.theme_use("clam")

janela.mainloop()
