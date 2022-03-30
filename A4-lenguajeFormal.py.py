import tkinter as tk
from tkinter import IntVar, ttk
from tkinter import messagebox
import random
import re


def limpiarCamposAbc():
    txAbcA.delete("1.0", "end")
    txAbcB.delete("1.0", "end")
    txABUnion.delete("1.0", "end")
    txBAminus.delete("1.0", "end")
    txABminus.delete("1.0", "end")
    txABInter.delete("1.0", "end")
    txABstar.delete("1.0", "end")
    txNstars.configure(bg = 'indian red')

def limpiarCamposLen():
    txLangA.delete("1.0", "end")
    txLangB.delete("1.0", "end")
    txLangABUnion.delete("1.0", "end")
    txLangABminus.delete("1.0", "end")
    txLangBAminus.delete("1.0", "end")
    txLangABInter.delete("1.0", "end")
    txLangABConcat.delete("1.0", "end")
    txABInver.delete("1.0", "end")
    txABPow.delete("1.0", "end")
    txNPow.configure( bg = 'indian red')
    lblLangBCardinal.configure(text = "Cardinal:")
    txWordsPerLang.configure( bg = 'indian red')
    
#clase conjunto
class Conjunto():
    def __init__(self):
        self.nombre = ""

    def generarLenguaje(self, abc, cant):
        palabra = ""
        palabras = ""
        num = 0

        rangoMax = 2
        palPos = len(abc)
        cantSim = len(abc)
        if cantSim == 0:
            return "ø"
        elif cantSim == 1:
            rangoMax = cant + 1
            if abc[0] == "ø":
                return "ø"
        else:
            while palPos < cant:
                rangoMax += 1
                palPos += pow(cantSim, rangoMax)

        while num < cant:
            ran = random.randint(2, rangoMax)
            
            for i in range(ran):
                palabra += random.choice(abc)

            if palabra not in palabras.split():
                palabras += " " + palabra
                num += 1
            palabra = ""

        return palabras.split()

class Alfabeto(Conjunto):
    def guardar(self, A, B):
        if (A == '') or (B == ''):
            messagebox.showwarning(message="Por favor ingrese dos alfabetos", title="Advertencia")
            return
        
        abcA = A.split()
        abcB = B.split()
        limpiarCamposAbc()
        limpiarCamposLen()
        self.operar(abcA, abcB)
        txAbcA.insert(1.0, abcA)
        txAbcB.insert(1.0, abcB)
        tabs.tab( 1, state = 'normal')
        tabs.tab( 2, state = 'normal')
        tabs.select(1)
        
        messagebox.showinfo(message="Alfabetos procesados con exíto", title="Hecho")
        
    def intersecar(self, A, B):
        interseccionAbc = []
        for sim in A:
            if sim in B:
                interseccionAbc.append(sim)
        if len(interseccionAbc) == 0:
            txABInter.insert(1.0, "ø")
        else:
            txABInter.insert(1.0, interseccionAbc)
            
    def restar(self, A, B):
        abcAMenosB = []
        abcBMenosA = []
        for sim in A:
            if sim not in B:
                abcAMenosB.append(sim)
                
        for sim in B:
            if sim not in A:
                abcBMenosA.append(sim)

        if len(abcAMenosB) == 0:
            txABminus.insert(1.0, "ø")
        else:
            txABminus.insert(1.0, abcAMenosB)
            
        if len(abcBMenosA) == 0:
            txBAminus.insert(1.0, "ø")
        else:
            txBAminus.insert(1.0, abcBMenosA)
        
    def unir(self, A, B):
        unionAbc = A[:]
        for sim in B:
            if sim not in unionAbc:
                unionAbc.append(sim)
        txABUnion.insert(1.0, unionAbc)
        
    
        
    def cerraduraEstrella(self, valor, cantidad, A, B, union):
        numValidate = re.compile('^\1?[0-9][0-9]*$')
        
        if not re.match(numValidate, cantidad):
            messagebox.showwarning(message="Por favor ingrese un número entero positivo.", title="Advertencia")
            txNstars.configure(bg = 'indian red')
            return
            
        txABstar.delete("1.0", "end")
        vector = []
        if valor == 1:
            vector = A.split()
        elif valor == 2:
            vector = B.split()
        else:
            vector = union.split()

        if int(cantidad) == 0:
            txABstar.insert(1.0, "ø")
        else:
            cerradura = self.generarLenguaje(vector, int(cantidad))
            txABstar.insert(1.0, cerradura)
        txNstars.configure( bg = 'spring green')
        
    def operar(self, A, B):
        self.unir(A, B)
        self.restar(A, B)
        self.intersecar(A, B)
    
class Lenguaje(Conjunto):
    def invertir(self, valor, A, B, union):
        txABInver.delete("1.0", "end")
        if valor == 1:
            vector = A.split()
        elif valor == 2:
            vector = B.split()
        else:
            vector = union.split()

        if len(vector) == 0:
            messagebox.showwarning(message="Por favor primero genere los lenguajes.", title="Advertencia")
            txNPow.configure( bg = 'indian red')
            return
        inverso = []
        aux = []
        for i in vector:
            aux.append(list(reversed(i)))

        palabras = ""
        for i in aux:
            for j in i:
                palabras += j
            palabras += " "
        inverso.extend(palabras.split())
        txABInver.insert(1.0, inverso)
    
    def potenciar(self, valor, potencia, A, B, union):
        numValidate = re.compile('^\1?[0-9][0-9]*$')

        if not re.match(numValidate, potencia):
            messagebox.showwarning(message="Por favor ingrese un número entero positivo.", title="Advertencia")
            txNPow.configure( bg = 'indian red')
            return
        
        txABPow.delete("1.0", "end")
        if valor == 1:
            vector = A.split()
        elif valor == 2:
            vector = B.split()
        else:
            vector = union.split()
            
        if len(vector) == 1 and vector[0] == "ø":
            txABPow.insert(1.0, "ø")
            txNPow.configure(bg = 'spring green')
            return

        if len(vector) == 0:
            messagebox.showwarning(message="Por favor primero genere los lenguajes.", title="Advertencia")
            txNPow.configure( bg = 'indian red')
            return

        vecPoten = []
        potencia = int(potencia)
        if potencia == 0:
            txABPow.insert(1.0, "ø")
        elif potencia == 1:
            txABPow.insert(1.0, vector)
        else:
            aux = vector
            vecPoten.extend(vector)
            for i in range(potencia - 1):      
                concatenacion = []
                for i in aux:
                    for j in vector: 
                        concatenacion.append(i+j)
                vecPoten.extend(concatenacion)
                aux = concatenacion
            txABPow.insert(1.0, vecPoten)
        txNPow.configure(bg = 'spring green')
        
    def concatenar(self, A, B):
        concatenacion = []
        for i in A:
            for j in B:
                concatenacion.append(i+j)
        i = 0
        while i < len(concatenacion): 
            concatenacion[i] = concatenacion[i].replace("ø","")
            i += 1
        txLangABConcat.insert(1.0, concatenacion)
        
    def intersecar(self, A, B):
        interseccionLan = []
        for sim in A:
            if sim in B:
                interseccionLan.append(sim)
        if len(interseccionLan) == 0:
            txLangABInter.insert(1.0, "ø")
        else:
            txLangABInter.insert(1.0, interseccionLan)
            
    def restar(self, A, B):
        lanAMenosB = []
        lanBMenosA = []
        for sim in A:
            if sim not in B:
                lanAMenosB.append(sim)
                
        for sim in B:
            if sim not in A:
                lanBMenosA.append(sim)

        if len(lanAMenosB) == 0:
            txLangABminus.insert(1.0, "ø")
        else:
            txLangABminus.insert(1.0, lanAMenosB)
            
        if len(lanBMenosA) == 0:
            txLangBAminus.insert(1.0, "ø")
        else:
            txLangBAminus.insert(1.0, lanBMenosA)
            
    def unir(self, A, B):
        unionLan = []
        if len(A) == 1 and A[0] == "ø":
            unionLan = A[:].split()
        else:
            unionLan = A[:]
        for sim in B:
            if sim not in unionLan:
                unionLan.append(sim)
        txLangABUnion.insert(1.0, unionLan)
        
    def guardar(self, cant, A, B):
        numValidate = re.compile('^\1?[0-9][0-9]*$')
        
        if not re.match(numValidate, cant):
            messagebox.showwarning(message="Por favor ingrese un número entero positivo.", title="Advertencia")
            txWordsPerLang.configure( bg = 'indian red')
            return

        lenA = self.generarLenguaje(A.split(), int(cant))
        lenB = self.generarLenguaje(B.split(), int(cant))
        limpiarCamposLen()
        self.operar(lenA, lenB)
        txLangA.insert(1.0, lenA)
        txLangB.insert(1.0, lenB)
        txWordsPerLang.configure(bg = 'spring green')
        lblLangACardinal.configure(text = "Cardinal: " + str(len(lenA)))
        lblLangBCardinal.configure(text = "Cardinal: " + str(len(lenB)))
        
    def operar(self, A, B):
        self.unir(A, B)
        self.restar(A, B)
        self.intersecar(A, B)
        self.concatenar(A, B)

def crearAbc(A, B):
    alf =  Alfabeto()
    alf.guardar(A, B)

def cerraduraEstrella(valor, cantidad, A, B, union):
    alf = Alfabeto()
    alf.cerraduraEstrella(valor, cantidad, A, B, union)
    
def crearLenguajes(cant, A, B):
    len = Lenguaje()
    len.guardar(cant, A, B)
    
def potenciar(valor, potencia, A, B, union):
    len = Lenguaje()
    len.potenciar(valor, potencia, A, B, union)
    
def invertir(valor, A, B, union):
    len = Lenguaje()
    len.invertir(valor, A, B, union)
    
    
def operateSets():
    arbol = 1

#Cracion de la ventana principal

def cambiarIdioma():
    if lblLang.cget('text') == 'es':

        btnSetLang.configure( text = 'Set language to Spanish.')
        lblWelcome.configure(text = "Welcome to the Formal Language Activity.")
        lblMsgHome.configure(text = "Enter two alphabets below. \nEach symbol separated by a space.\n For empty use: ø (alt + 0248)")
        btnRun.configure(text = "Start")
        frmAbcs.configure(text = "Alphabet")
        frmABUnion.configure(text = "Union (AuB)")
        frmABDif.configure(text = "Difference (A-B) and (B-A)")
        frmABIntercept.configure(text = "Intercept (A∩B)")
        frmABstar.configure(text = "Star lock")
        lblLang.configure(text = 'en')
        
    else:
        btnSetLang.configure( text = 'Cambiar idioma a ingles.')
        lblWelcome.configure(text = "Bienvenido a la Actividad de lenguaje formal.")
        lblMsgHome.configure(text = "A continuación ingrese dos alfabetos.\nCada simbolo separado por un espacio. \n para vacio use: ø (alt + 0248)")
        btnRun.configure(text = "Empezar a operar")
        frmAbcs.configure(text = "Alfabeto")
        frmABUnion.configure(text = "Union (AuB)")
        frmABDif.configure(text = "Diferencia (A-B) y (B-A)")
        frmABIntercept.configure(text = "Intercepción (A∩B)")
        frmABstar.configure(text = "Generar cerradura de estrella")
        lblLang.configure( text = 'es')
        btnSetLang.configure( text = 'Cambiar idioma a Ingles.')
        
  
    
    
    
        
window = tk.Tk()
window.title('Actividad 4 - LenguajesFormales')
window.geometry("1024x800+50+50")
window.minsize(1000,800)
window.configure(bg = "DarkSlateGrey")
btnSetLang = tk.Button(window, text = "Cambiar idioma a Ingles.", command = cambiarIdioma)
lblLang = lblWelcome = tk.Label(window, text="es")
btnSetLang.place(x = 15, y = 15)

#creando las pestañas
tabs = ttk.Notebook(window)
tabs.pack()

#Home tab
frmHome = tk.Frame(tabs, padx = 20 , pady = 20)
tabs.add(frmHome, text = "Inicio")

lblWelcome = tk.Label(frmHome, text="Bienvenido a la Actividad de lenguaje formal.", fg="blue", font=("Comic Sans MS", 15) )
lblWelcome.pack()
lblMsgHome = tk.Label(frmHome, text="A continuación ingrese dos alfabetos.\nCada simbolo separado por un espacio. \n para vacio use: ø (alt + 0248)", fg="black", font=("Comic Sans MS", 12))
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

btnRun = tk.Button(frmHome, text = "Empezar a operar", command=lambda: crearAbc(inAbc1.get(), inAbc2.get()))
btnRun.pack()

#Alphabet tab
frmAlphabet = ttk.Frame(tabs, padding= '20px')
tabs.add(frmAlphabet, text = "Alfabetos", state = 'disabled')

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
opt.set(1)
tk.Radiobutton(frmABstar, text="(A)*", variable=opt, value=1).grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmABstar, text="(B)*", variable=opt, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmABstar, text="(AuB)*", variable=opt, value=3).grid(row = 0, column = 2, pady = 5)
txNstars = tk.Text(frmABstar, height = 1, width = 5, bg = "indian red")
txNstars.grid(row = 1, column = 0, pady = 5)
tk.Button(frmABstar, text = "Generar cerradura de estrella", command=lambda: cerraduraEstrella(opt.get(), txNstars.get("1.0", "end"), txAbcA.get("1.0", "end"), txAbcB.get("1.0", "end"), txABUnion.get("1.0", "end"))).grid(row = 1, column = 1, pady = 5)

lblABstar = tk.Label(frmABstar, text="(...)*:", fg="black", font=("Comic Sans MS", 10))
lblABstar.grid( row = 2, column = 0, pady = 5)
txABstar = tk.Text(frmABstar, height = 5, width = 20)
txABstar.bind("<Key>", lambda readOnly: "break")
txABstar.grid(row = 2, column = 1, pady = 5,columnspan = 2)

#Language tab
frmlanguage= ttk.Frame(tabs, padding= '20px')
tabs.add(frmlanguage, text = "Lenguajes", state = 'disabled')

frmLangs =ttk.Labelframe(frmlanguage, padding= '10px', text="Sea LA y LB lenguajes:")
frmLangs.pack(fill = 'both')

lblWordsPerLang = tk.Label(frmLangs, text="Inserte la cantidad de \n palabras para los lenguajes:", fg="red", font=("Comic Sans MS", 10))
lblWordsPerLang.grid( row = 0, column = 0, pady = 5)
txWordsPerLang = tk.Text(frmLangs, height = 1, width = 10, bg = "indian red")
txWordsPerLang.grid(row = 0, column = 1, pady = 5)

tk.Button(frmLangs, text = "Generar lenguajes", command=lambda: crearLenguajes(txWordsPerLang.get("1.0", "end"), txAbcA.get("1.0", "end"), txAbcB.get("1.0", "end"))).grid(row = 0, column = 2, pady = 5)

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

lblLangABConcat = tk.Label(frmLangABConcat, text="(LA.LB):", fg="black", font=("Comic Sans MS", 10))
lblLangABConcat.grid( row = 0, column = 0, pady = 5)
txLangABConcat = tk.Text(frmLangABConcat, height = 2, width = 20)
txLangABConcat.bind("<Key>", lambda readOnly: "break")
txLangABConcat.grid(row = 0, column = 1, pady = 5)

frmLangABPow = ttk.Labelframe(frmOperationLang, padding= '10px', text="Potencia de lenguajes")
frmLangABPow.grid(row = 2, column = 0, sticky = 'nsew', padx = 2)

opt2 = IntVar()
opt2.set(1)
tk.Radiobutton(frmLangABPow, text="(LA)^n", variable=opt2, value=1, state ='active').grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmLangABPow, text="(LB)^n", variable=opt2, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmLangABPow, text="(LAuLB)^n", variable=opt2, value=3).grid(row = 0, column = 2, pady = 5)
txNPow = tk.Text(frmLangABPow, height = 1, width = 7, bg = "indian red")
txNPow.grid(row = 1, column = 0, pady = 5)
tk.Button(frmLangABPow, text = "Generar Potencia", command=lambda: potenciar(opt2.get(), txNPow.get("1.0", "end"), txLangA.get("1.0", "end"), txLangB.get("1.0", "end"), txLangABUnion.get("1.0", "end"))).grid(row = 1, column = 1, pady = 5)

lblABPow = tk.Label(frmLangABPow, text="(...)^n:", fg="black", font=("Comic Sans MS", 10))
lblABPow.grid( row = 2, column = 0, pady = 5)
txABPow = tk.Text(frmLangABPow, height = 5, width = 20)
txABPow.bind("<Key>", lambda readOnly: "break")
txABPow.grid(row = 2, column = 1, pady = 5, columnspan = 2)

frmLangABInver = ttk.Labelframe(frmOperationLang, padding= '10px', text="Invertir Lenguaje")
frmLangABInver.grid(row = 2, column = 1, sticky = 'nsew')

opt3 = IntVar()
opt3.set(1)
asas = tk.Radiobutton(frmLangABInver, text="(LA)^-1", variable=opt3, value=1, state ='active', ).grid(row = 0, column = 0, pady = 5)
tk.Radiobutton(frmLangABInver, text="(LB)^-1", variable=opt3, value=2).grid(row = 0, column = 1, pady = 5)
tk.Radiobutton(frmLangABInver, text="(LAuLB)^-1", variable=opt3, value=3).grid(row = 0, column = 2, pady = 5)
tk.Button(frmLangABInver, text = "Generar Inversa", command=lambda: invertir(opt3.get(), txLangA.get("1.0", "end"), txLangB.get("1.0", "end"), txLangABUnion.get("1.0", "end"))).grid(row = 1, column = 1, pady = 5)

lblABInver = tk.Label(frmLangABInver, text="(...)^-1:", fg="black", font=("Comic Sans MS", 10))
lblABInver.grid( row = 2, column = 0, pady = 5)
txABInver = tk.Text(frmLangABInver, height = 5, width = 20)
txABInver.bind("<Key>", lambda readOnly: "break")
txABInver.grid(row = 2, column = 1, pady = 5, columnspan = 2)

#tabs.tab( 2, state = 'normal')
tabs.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
window.mainloop()
