#ANALISE EST COVID LATINAMERICA
from tkinter import Button, Label, StringVar, Tk
from tkinter.constants import LEFT, W
from openpyxl import load_workbook

WORKBOOK, WORKSHEET = "COVID-19_01062021.xlsx", "Planilha1"

wb = load_workbook(WORKBOOK)
ws = wb[WORKSHEET]

app = Tk() 
app.title("COVID NA AMÉRICA LATINA")
app.geometry("300x200")
app.configure(background="#dde")

self.label = tkinter.Label(self.main_window, text='Curso Python Progressivo!' )

def BOL():
    DADOS_BOL = [20,40,60]
    print('O MAIOR VALOR NA BOLÍVIA FOI DE :', max(DADOS_BOL))

def BRA():
    DADOS_BRA = [30,20,10]
    print('O MAIOR VALOR NO BRASIL FOI DE :', max(DADOS_BRA))

def CHI():
    DADOS_CHI=[90,120,250]
    print('O MAIOR VALOR NO CHILE FOI DE :', max(DADOS_CHI))

#ANALISE 
Label(app, text="Qual o país? :", background="#dde", foreground="#009", anchor=W).place(x=10, y=30)

#Botao BOL
btnC = Button(app, text="BOL", fg="red", command=BOL)
btnC.pack(side = LEFT)

#Botao BRA
btnF = Button(app, text="BRA", fg="blue", command=BRA)
btnF.pack(side = LEFT)

#Botao CHI
btnF = Button(app, text="CHI", fg="green", command=CHI)
btnF.pack(side = LEFT)
app.mainloop()