import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

#abecedarios y lenguajes
abcA = ""
abcB = ""
lenA = ""
lenB = ""

#generar lenguaje
def generarLenguaje(abc):
    palabra = ""
    palabras = ""
    num = 0
    
    while num < 5:
        ran = random.randint(2, 5)
        
        for i in range(ran):
            palabra += random.choice(abc)

        if palabra not in palabras.split():
            palabras += " " + palabra
            num += 1
        palabra = ""

    return palabras.split()

#guardar lenguajes
def guardarLenguajes(A, B):
    lenA = generarLenguaje(A)
    lenB = generarLenguaje(B)
        
#guardar abecedarios
def guardarAbecedarios(A, B):
    abcA = A.split()
    abcB = B.split()
    txAbcA.insert(1.0, abcA)
    guardarLenguajes(abcA, abcB)
    tabs.tab( 1, state = 'normal')
    tabs.tab( 2, state = 'normal')
    tabs.select(1)
    
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


frmAbcs = ttk.Labelframe(frmAlphabet, padding= '10px', text="Alfabetos:")
frmAbcs.pack(fill = 'both')

lblA = tk.Label(frmAbcs, text="A: ", fg="black", font=("Comic Sans MS", 10))
lblA.grid( row = 0, column = 0, pady = 5)
txAbcA = tk.Text(frmAbcs, height = 2, width = 20)
txAbcA.bind("<Key>", lambda readOnly: "break")
txAbcA.grid(row = 0, column = 1, pady = 5)

lblB = tk.Label(frmAbcs, text="B: ", fg="black", font=("Comic Sans MS", 10))
lblB.grid( row = 0, column = 2, pady = 5)
txAbcB = tk.Text(frmAbcs, height = 2, width = 20)
txAbcB.bind("<Key>", lambda readOnly: "break")
txAbcB.grid(row = 0, column = 3, pady = 5)

frmOperation = ttk.Frame(frmAlphabet, padding= '5px')
frmOperation.pack()

frmABUnion = ttk.Labelframe(frmOperation, padding= '10px', text="Unión (AuB)")
frmABUnion.grid(row = 0, column = 0, padx = 2, sticky = 'nsew')

lblABUnion = tk.Label(frmABUnion, text="(A+B):", fg="black", font=("Comic Sans MS", 10))
lblABUnion.grid( row = 0, column = 0, pady = 5)
txABUnion = tk.Text(frmABUnion, height = 2, width = 20)
txABUnion.bind("<Key>", lambda readOnly: "break")
txABUnion.grid(row = 0, column = 1, pady = 5)

frmABDif = ttk.Labelframe(frmOperation, padding= '10px', text="Diferencia (A-B) & (B-A)")
frmABDif.grid(row = 0, column = 1, sticky = 'nsew')

lblABminus = tk.Label(frmABDif, text="(A-B):", fg="black", font=("Comic Sans MS", 10))
lblABminus.grid( row = 0, column = 0, pady = 5)
txABminus = tk.Text(frmABDif, height = 2, width = 20)
txABminus.bind("<Key>", lambda readOnly: "break")
txABminus.grid(row = 0, column = 1, pady = 5)

lblBAminus = tk.Label(frmABDif, text="(B-A):", fg="black", font=("Comic Sans MS", 10))
lblBAminus.grid( row = 1, column = 0, pady = 5)
txBAminus = tk.Text(frmABDif, height = 2, width = 20)
txBAminus.bind("<Key>", lambda readOnly: "break")
txBAminus.grid(row = 1, column = 1, pady = 5)

frmABIntercept = ttk.Labelframe(frmOperation, padding= '10px', text="Intercepción (A∩B)")
frmABIntercept.grid(row = 1, column = 0, sticky = 'nsew', padx = 2)

lblABInter = tk.Label(frmABIntercept, text="(A∩B):", fg="black", font=("Comic Sans MS", 10))
lblABInter.grid( row = 0, column = 0, pady = 5)
txABInter = tk.Text(frmABIntercept, height = 2, width = 20)
txABInter.bind("<Key>", lambda readOnly: "break")
txABInter.grid(row = 0, column = 1, pady = 5)

frmABstar = ttk.Labelframe(frmOperation, padding= '10px', text="Cerradura de Estrella")
frmABstar.grid(row = 1, column = 1, sticky = 'nsew')

lblABstar = tk.Label(frmABstar, text="(A∩B):", fg="black", font=("Comic Sans MS", 10))
lblABstar.grid( row = 0, column = 0, pady = 5)
txABstar = tk.Text(frmABIntercept, height = 2, width = 20)
txABstar.bind("<Key>", lambda readOnly: "break")
txABstar.grid(row = 0, column = 1, pady = 5)



tabs.add(frmAlphabet, text = "Alfabetos")

#Language tab
frmlanguage= ttk.Frame(tabs, padding= '20px')
lbllanguage = tk.Label(frmlanguage, text="Lenguajes", fg="black")
lbllanguage.pack()
id = tabs.add(frmlanguage, text = "Lenguajes")

#tabs.tab( 2, state = 'normal')
tabs.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
window.mainloop()