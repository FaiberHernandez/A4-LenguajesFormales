import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import NoteBook

#guardar abecedarios
def guardarAbecedarios(A, B):
    abcA = A.split()
    abcB = B.split()

    print("Abecedario A:")
    for i in abcA:
        print(i)

    print("\nAbecedario B:")
    for i in abcB:
        print(i)
    
def operateSets():
    arbol = 1

window = tk.Tk()
window.title('Actividad 4 - LenguajesFormales')
window.geometry("800x600+0+0")
window.minsize(800, 600)

tabs = ttk.Notebook(window)
tabs.pack()

#Home tab
frmHome = tk.Frame(tabs, padx = 20 , pady = 20)

lblWelcome = tk.Label(frmHome, text="Bienvenido a la Actividad de lenguaje formal.", fg="blue", font=("Comic Sans MS", 15) )
lblWelcome.pack()
lblMsgHome = tk.Label(frmHome, text="A continuación ingrese dos alfabetos.\nCada simbolo separado por un espacio.", fg="black", font=("Comic Sans MS", 12))
lblMsgHome.pack()

#Home Inputs
iniInputs = tk.Frame(frmHome, padx = 20 , pady = 20)
iniInputs.pack()

lblAbc1 = tk.Label(iniInputs, text="A: ", fg="black", font=("Comic Sans MS", 10))
lblAbc1.grid( row = 0, column = 0, pady = 5)
inAbc1 = tk.Entry(iniInputs)
inAbc1.grid( row = 0, column = 1, pady = 5)

lblAbc2 = tk.Label(iniInputs, text="B: ", fg="black", font=("Comic Sans MS", 10))
lblAbc2.grid( row = 1, column = 0, pady = 5)
inAbc2 = tk.Entry(iniInputs)
inAbc2.grid( row = 1, column = 1, pady = 5)

btnRun = tk.Button(frmHome, text = "Empezar a operar", command=lambda: guardarAbecedarios(inAbc1.get(), inAbc2.get()))
btnRun.pack()

tabs.add(frmHome, text = "Inicio")

#Alphabet tab
frmAlphabet = ttk.Frame(tabs, padding= '20px')
lblAlphabet = tk.Label(frmAlphabet, text="Alfabetos", fg="black")
lblAlphabet.pack()
tabs.add(frmAlphabet, text = "Alfabetos", state= 'disabled')

#Language tab
frmlanguage= ttk.Frame(tabs, padding= '20px')
lbllanguage = tk.Label(frmlanguage, text="Lenguajes", fg="black")
lbllanguage.pack()
id = tabs.add(frmlanguage, text = "Lenguajes", state= 'disabled')

#tabs.tab( 2, state = 'normal')
tabs.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
window.mainloop()


