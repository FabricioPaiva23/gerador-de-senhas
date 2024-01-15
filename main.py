from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import string
import random

cor0 = "#444466"
cor1 = "#feffff"
cor3 = "#f05a43"

janela = Tk()
janela.title("Gerador de senha")
janela.geometry("295x350")
janela.configure(bg=cor1)

frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief=FLAT)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

estilo = ttk.Style(janela)

img = Image.open("password.png")

img = img.resize((45,45), Image.Resampling.LANCZOS)

img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief=FLAT, anchor=NW, bg=cor1)
app_logo.place(x=2, y=0)

app_texto = Label(frame_cima, text="Gerador de senhas", height=60, padx=10, relief=FLAT,font=("Ivi 15 bold"), anchor=NW, bg=cor1, fg=cor0)
app_texto.place(x=60, y=10)

app_linha = Label(frame_cima, width=295, height=1, padx=10, relief=FLAT,font=("Ivi 1"), anchor=NW, bg=cor3, fg=cor0)
app_linha.place(x=0, y=45)

app_senha = Label(frame_baixo, text="- - -", width=25, height=2, padx=0, relief=SOLID,font=("Ivi 10 bold"), anchor=CENTER, bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text="Número de caracteres", height=1, padx=0, relief=FLAT,font=("Ivi 10 bold"), anchor=NW, bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW,padx=5, pady=8 )

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()!@#$%*&?_-'

frame_caractere = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, padx=0, relief=FLAT)
frame_caractere.grid(row=3, column=0, sticky=NSEW)

estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caractere, width=1, var=estado_1, onvalue=alfa_maior, offvalue='off', bg=cor1, relief=FLAT )
check_1.grid(row=0, column=0, sticky=NW,padx=2, pady=5)

app_ = Label(frame_caractere, text="ABC - Letras maiusculas", height=1, padx=0, relief=FLAT,font=("Ivi 10 bold"), anchor=NW, bg=cor1, fg=cor0)
app_.grid(row=0, column=1, sticky=NW, padx=2, pady=5)


estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caractere, width=1, var=estado_2, onvalue=alfa_menor, offvalue='off', bg=cor1, relief=FLAT )
check_2.grid(row=1, column=0, sticky=NW,padx=2, pady=5)

app_ = Label(frame_caractere, text="abc - Letras minusculas", height=1, padx=0, relief=FLAT,font=("Ivi 10 bold"), anchor=NW, bg=cor1, fg=cor0)
app_.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caractere, width=1, var=estado_3, onvalue=numeros, offvalue='off', bg=cor1, relief=FLAT )
check_3.grid(row=2, column=0, sticky=NW,padx=2, pady=5)

app_ = Label(frame_caractere, text="123 - Números", height=1, padx=0, relief=FLAT,font=("Ivi 10 bold"), anchor=NW, bg=cor1, fg=cor0)
app_.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caractere, width=1, var=estado_4, onvalue=simbolos, offvalue='off', bg=cor1, relief=FLAT )
check_4.grid(row=3, column=0, sticky=NW,padx=2, pady=5)

app_ = Label(frame_caractere, text="!@# - Símbolos", height=1, padx=0, relief=FLAT,font=("Ivi 10 bold"), anchor=NW, bg=cor1, fg=cor0)
app_.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

botao_senha = Button(frame_caractere, text="Gerar Senha", width=30, height=1, relief=FLAT,font=("Ivi 10 bold"), overrelief=SOLID, anchor=CENTER, bg=cor3, fg=cor1)
botao_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=0, columnspan=5)




janela.mainloop()
