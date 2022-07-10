from tkinter import * 


app = Tk() 
app.title("Conversor F <-> C")
app.geometry("300x200")
app.configure(background="#dde")

def cel_fahr():
    F = float(vT.get()) * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))
    
    if F < 50:
        print("PERIGO!!!!")
    elif F > 95:
        print("PERIGO!!!!")
    else:
        print("TEMPERATURA NORMAL")

def fahr_cel():
    C = (float(vT.get()) - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))
    
    if C < 10:
        print("PERIGO!!!!")
    elif C > 35:
        print("PERIGO!!!!")
    else:
        print("TEMPERATURA NORMAL")

#TEMPERATURA 
Label(app, text="Temperatura :", background="#dde", foreground="#009", anchor=W).place(x=10, y=30)


#Botao Celsius
btnC = Button(app, text="C -> F", fg="red", command=cel_fahr)
btnC.pack(side = LEFT)

#Botao Fahrenheit
btnF = Button(app, text="F -> C", fg="blue", command=fahr_cel)
btnF.pack(side = LEFT)
app.mainloop()