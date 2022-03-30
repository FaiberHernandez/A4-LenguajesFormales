import tkinter as tk
from tkinter import IntVar, ttk
from tkinter import messagebox
import random
import itertools
from itertools import product

#intersecar abecedarios
def intersecarAbc(A, B):
    interseccionAbc = []
    for sim in A:
        if sim in B:
            interseccionAbc.append(sim)
    if len(interseccionAbc) == 0:
        txABInter.insert(1.0, "¢")
    else:
        txABInter.insert(1.0, interseccionAbc)

#restar abecedarios
def restarAbc(A, B):
    abcAMenosB = []
    abcBMenosA = []
    for sim in A:
        if sim not in B:
            abcAMenosB.append(sim)
            
    for sim in B:
        if sim not in A:
            abcBMenosA.append(sim)

    if len(abcAMenosB) == 0:
        txABminus.insert(1.0, "¢")
    else:
        txABminus.insert(1.0, abcAMenosB)
        
    if len(abcBMenosA) == 0:
        txBAminus.insert(1.0, "¢")
    else:
        txBAminus.insert(1.0, abcBMenosA)
            
#unir abecedarios
def unirAbc(A, B):
    unionAbc = A[:]
    for sim in B:
        if sim not in unionAbc:
            unionAbc.append(sim)
    txABUnion.insert(1.0, unionAbc)

#operar abecedarios
def operarAbc(A, B):
    unirAbc(A, B)
    restarAbc(A, B)
    intersecarAbc(A, B)

#generar lenguaje
def generarLenguaje(abc, cant):
    palabra = ""
    palabras = ""
    num = 0
    
    while num < cant:
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
    global lenA
    lenA = generarLenguaje(A, 5)
    lenB = generarLenguaje(B, 5)

#limpiar campos
def limpiarCampos():
    txAbcA.delete("1.0", "end")
    txAbcB.delete("1.0", "end")
    txABUnion.delete("1.0", "end")
    txBAminus.delete("1.0", "end")
    txABminus.delete("1.0", "end")
    txABInter.delete("1.0", "end")
    txABstar.delete("1.0", "end")

#cerradura estrella
def cerraduraEstrella(valor, cantidad, A, B, union):
    txABstar.delete("1.0", "end")
    vector = []
    if valor == 1:
        vector = A.split()
    elif valor == 2:
        vector = B.split()
    else:
        vector = union.split()
        
    cerradura = generarLenguaje(vector, int(cantidad))
    txABstar.insert(1.0, cerradura)
        
#guardar abecedarios
def guardarAbecedarios(A, B):
    abcA = A.split()
    abcB = B.split()
    guardarLenguajes(abcA, abcB)
    limpiarCampos()
    operarAbc(abcA, abcB)
    txAbcA.insert(1.0, abcA)
    txAbcB.insert(1.0, abcB)
    tabs.tab( 1, state = 'normal')
    tabs.tab( 2, state = 'normal')
    tabs.select(1)
        
def operateSets():
    arbol = 1

#Cracion de la ventana principal
window = tk.Tk()
window.title('Actividad 4 - LenguajesFormales')
window.geometry("1024x800+50+50")
window.minsize(1000,800)
window.configure(bg = "DarkSlateGrey")

#creando las pestañas
tabs = ttk.Notebook(window)
tabs.pack()

#Home tab
frmHome = tk.Frame(tabs, padx = 20 , pady = 20)
tabs.add(frmHome, text = "Inicio")

lblWelcome = tk.Label(frmHome, text="Bienvenido a la Actividad de lenguaje formal.", fg="blue", font=("Comic Sans MS", 15) )
lblWelcome.pack()
lblMsgHome = tk.Label(frmHome, text="A continuación ingrese dos alfabetos.\nCada simbolo separado por un espacio. \n para vacio use: ¢ (alt + 155)", fg="black", font=("Comic Sans MS", 12))
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

#Alphabet tab
frmAlphabet = ttk.Frame(tabs, padding= '20px')
tabs.add(frmAlphabet, text = "Alfabetos")

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

frmABDif = ttk.Labelframe(frmOperation, padding= '10px', text="Diferencia (A-B) y (B-A)")
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

opt = IntVar()
tk.Radiobutton(frmABstar, text="(A)*", variable=opt, value=1).grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmABstar, text="(B)*", variable=opt, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmABstar, text="(AuB)*", variable=opt, value=3).grid(row = 0, column = 2, pady = 5)
txNstars = tk.Text(frmABstar, height = 1, width = 5)
txNstars.grid(row = 1, column = 0, pady = 5)
tk.Button(frmABstar, text = "Generar cerradura de estrella", command=lambda: cerraduraEstrella(opt.get(), txNstars.get("1.0", "end"), txAbcA.get("1.0", "end"), txAbcB.get("1.0", "end"), txABUnion.get("1.0", "end"))).grid(row = 1, column = 1, pady = 5)

lblABstar = tk.Label(frmABstar, text="(...)*:", fg="black", font=("Comic Sans MS", 10))
lblABstar.grid( row = 2, column = 0, pady = 5)
txABstar = tk.Text(frmABstar, height = 5, width = 20)
txABstar.bind("<Key>", lambda readOnly: "break")
txABstar.grid(row = 2, column = 1, pady = 5,columnspan = 2)



#Language tab
frmlanguage= ttk.Frame(tabs, padding= '20px')
tabs.add(frmlanguage, text = "Lenguajes")

frmLangs =ttk.Labelframe(frmlanguage, padding= '10px', text="Sea LA y LB lenguajes:")
frmLangs.pack(fill = 'both')


lblWordsPerLang = tk.Label(frmLangs, text="Inserte la cantidad de \n palabras para los lenguajes:", fg="red", font=("Comic Sans MS", 10))
lblWordsPerLang.grid( row = 0, column = 0, pady = 5)
txWordsPerLang = tk.Text(frmLangs, height = 1, width = 10)
txWordsPerLang.grid(row = 0, column = 1, pady = 5)

tk.Button(frmLangs, text = "Generar lenguajes").grid(row = 0, column = 2, pady = 5)


lblLangA = tk.Label(frmLangs, text="LA: ", fg="black", font=("Comic Sans MS", 10))
lblLangA.grid( row = 1, column = 0, pady = 5)
txLangA = tk.Text(frmLangs, height = 2, width = 20)
txLangA.bind("<Key>", lambda readOnly: "break")
txLangA.grid(row = 1, column = 1, pady = 5)

lblLangACardinal = tk.Label(frmLangs, text="Cardinal: ", fg="green", font=("Comic Sans MS", 10))
lblLangACardinal.grid( row = 2, column = 0)

lblLangB = tk.Label(frmLangs, text="LB: ", fg="black", font=("Comic Sans MS", 10))
lblLangB.grid( row = 1, column = 2, pady = 5)
txLangB = tk.Text(frmLangs, height = 2, width = 20)
txLangB.bind("<Key>", lambda readOnly: "break")
txLangB.grid(row = 1, column = 3, pady = 5)

lblLangBCardinal = tk.Label(frmLangs, text="Cardinal: ", fg="green", font=("Comic Sans MS", 10))
lblLangBCardinal.grid( row = 2, column = 2)


frmOperationLang = ttk.Frame(frmlanguage, padding= '5px')
frmOperationLang.pack()

frmLangABUnion = ttk.Labelframe(frmOperationLang, padding= '10px', text="Unión (LA+LB)")
frmLangABUnion.grid(row = 0, column = 0, padx = 2, sticky = 'nsew')

lblLangABUnion = tk.Label(frmLangABUnion, text="(LA+LB):", fg="black", font=("Comic Sans MS", 10))
lblLangABUnion.grid( row = 0, column = 0, pady = 5)
txLangABUnion = tk.Text(frmLangABUnion, height = 2, width = 20)
txLangABUnion.bind("<Key>", lambda readOnly: "break")
txLangABUnion.grid(row = 0, column = 1, pady = 5)

frmLangABDif = ttk.Labelframe(frmOperationLang, padding= '10px', text="Diferencia (LA-LB) y (LB-LA)")
frmLangABDif.grid(row = 0, column = 1, sticky = 'nsew')

lblLangABminus = tk.Label(frmLangABDif, text="(LA-LB):", fg="black", font=("Comic Sans MS", 10))
lblLangABminus.grid( row = 0, column = 0, pady = 5)
txLangABminus = tk.Text(frmLangABDif, height = 2, width = 20)
txLangABminus.bind("<Key>", lambda readOnly: "break")
txLangABminus.grid(row = 0, column = 1, pady = 5)

lblLangBAminus = tk.Label(frmLangABDif, text="(LB-LA):", fg="black", font=("Comic Sans MS", 10))
lblLangBAminus.grid( row = 1, column = 0, pady = 5)
txLangBAminus = tk.Text(frmLangABDif, height = 2, width = 20)
txLangBAminus.bind("<Key>", lambda readOnly: "break")
txLangBAminus.grid(row = 1, column = 1, pady = 5)

frmLangABIntercept = ttk.Labelframe(frmOperationLang, padding= '10px', text="Intercepción (LA∩LB)")
frmLangABIntercept.grid(row = 1, column = 0, sticky = 'nsew', padx = 2)

lblLangABInter = tk.Label(frmLangABIntercept, text="(LA∩LB):", fg="black", font=("Comic Sans MS", 10))
lblLangABInter.grid( row = 0, column = 0, pady = 5)
txLangABInter = tk.Text(frmLangABIntercept, height = 2, width = 20)
txLangABInter.bind("<Key>", lambda readOnly: "break")
txLangABInter.grid(row = 0, column = 1, pady = 5)

frmLangABConcat = ttk.Labelframe(frmOperationLang, padding= '10px', text="Cocatenación (LA.LB)")
frmLangABConcat.grid(row = 1, column = 1, sticky = 'nsew', padx = 2)

lblLangABConcat = tk.Label(frmLangABConcat, text="(LALB):", fg="black", font=("Comic Sans MS", 10))
lblLangABConcat.grid( row = 0, column = 0, pady = 5)
txLangABConcat = tk.Text(frmLangABConcat, height = 2, width = 20)
txLangABConcat.bind("<Key>", lambda readOnly: "break")
txLangABConcat.grid(row = 0, column = 1, pady = 5)

frmLangABPow = ttk.Labelframe(frmOperationLang, padding= '10px', text="Potencia de lenguajes")
frmLangABPow.grid(row = 2, column = 0, sticky = 'nsew')

opt2 = IntVar()
tk.Radiobutton(frmLangABPow, text="(LA)^n", variable=opt2, value=1).grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmLangABPow, text="(LB)^n", variable=opt2, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmLangABPow, text="(LAuLB)^n", variable=opt2, value=3).grid(row = 0, column = 2, pady = 5)
txNPow = tk.Text(frmLangABPow, height = 1, width = 7)
txNPow.grid(row = 1, column = 0, pady = 5)
tk.Button(frmLangABPow, text = "Generar Potencia").grid(row = 1, column = 1, pady = 5)

lblABPow = tk.Label(frmLangABPow, text="(...)^n:", fg="black", font=("Comic Sans MS", 10))
lblABPow.grid( row = 2, column = 0, pady = 5)
txABPow = tk.Text(frmLangABPow, height = 5, width = 20)
txABPow.bind("<Key>", lambda readOnly: "break")
txABPow.grid(row = 2, column = 1, pady = 5, columnspan = 2)

frmLangABInver = ttk.Labelframe(frmOperationLang, padding= '10px', text="Lenguajes Invertidos")
frmLangABInver.grid(row = 2, column = 1, sticky = 'nsew')

opt3 = IntVar()
tk.Radiobutton(frmLangABInver, text="(LA)^-1", variable=opt3, value=1).grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmLangABInver, text="(LB)^-1", variable=opt3, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmLangABInver, text="(LAuLB)^-1", variable=opt3, value=3).grid(row = 0, column = 2, pady = 5)
txNInver = tk.Text(frmLangABInver, height = 1, width = 7)
txNInver.grid(row = 1, column = 0, pady = 5)
tk.Button(frmLangABInver, text = "Generar Ineversa").grid(row = 1, column = 1, pady = 5)

lblABInver = tk.Label(frmLangABInver, text="(...)^-1:", fg="black", font=("Comic Sans MS", 10))
lblABInver.grid( row = 2, column = 0, pady = 5)
txABInver = tk.Text(frmLangABInver, height = 5, width = 20)
txABInver.bind("<Key>", lambda readOnly: "break")
txABInver.grid(row = 2, column = 1, pady = 5, columnspan = 2)




#tabs.tab( 2, state = 'normal')
tabs.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
window.mainloop()
