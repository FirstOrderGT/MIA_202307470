import tkinter as tk
import tkmacosx as tkm
from tkinter import simpledialog
from Estructuras.ListaContigua import ListaContigua
from Estructuras.ListaDoble import ListaDoble
from Estructuras.ListaSimple import ListaSimple
from Estructuras.ListaIndex import ListaIndex

listaSeleccionada = None
liContigua = None
liSimple = None
liDoble = None
liIndex = None

def ActContigua():
    global listaSeleccionada, liContigua
    if liContigua is None:
        size = simpledialog.askinteger('Capacidad de la lista', 'Ingrese un valor:')
        if size:
            liContigua = ListaContigua(size)
            listaSeleccionada = liContigua
    else:
        listaSeleccionada = liContigua

def ActSimple():
    global listaSeleccionada, liSimple
    if liSimple is None:
        liSimple = ListaSimple()
        listaSeleccionada = liSimple
    else:
        listaSeleccionada = liSimple

def ActDoble():
    global listaSeleccionada, liDoble
    if liDoble is None:
        liDoble = ListaDoble()
        listaSeleccionada = liDoble
    else:
        listaSeleccionada = liDoble

def ActIndex():
    global listaSeleccionada, liIndex
    if liIndex is None:
        liIndex = ListaIndex()
        listaSeleccionada = liIndex
    else:
        listaSeleccionada = liIndex

def insertar():
    datoInsertar = campoDato.get().strip()

    listaSeleccionada.insertar(datoInsertar)

def eliminar():
    datoEliminar = campoDato.get().strip()

    listaSeleccionada.eliminar(datoEliminar)

def mostrar():
    entrada.delete("1.0", tk.END)
    entrada.insert(tk.END, listaSeleccionada.mostrar()) 

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.geometry("900x700+300+100")
ventana.state('zoomed')
ventana.title("Practica 1")
ventana.config(bg='#aaafc1')
ventana.minsize(900, 700)

tk.Label(ventana, text="Contenido de la lista: ", bg='#aaafc1', fg='black').place(x=10, y=50)
entrada = tk.Text(ventana, height=40, width=60)
entrada.place(x=10, y=80)

tk.Label(ventana, text="Dato:").place(x=500, y=370)
campoDato = tk.Entry(ventana, width=30)
campoDato.place(x=500, y=400)
tkm.Button(ventana, text="Insertar", command=insertar, bg='white', fg='black', borderless=1, relief='flat').place(x=500, y=450)
tkm.Button(ventana, text="Eliminar", command=eliminar, bg='white', fg='black', borderless=1, relief='flat').place(x=600, y=450)
tkm.Button(ventana, text="Mostrar", command=mostrar, bg='white', fg='black', borderless=1, relief='flat').place(x=500, y=500)
tkm.Button(ventana, text="Salir", command=salir, bg='white', fg='black', borderless=1, relief='flat').place(x=500, y=550)

tk.Label(ventana, text="Escoga una lista: ", bg='#aaafc1', fg='black').place(x=450, y=50)
tkm.Button(ventana, text="Lista Contigua", command=ActContigua, bg='white', fg='black', borderless=1, relief='flat').place(x=450, y=80)
tkm.Button(ventana, text="Lista Simple", command=ActSimple, bg='white', fg='black', borderless=1, relief='flat').place(x=585, y=80)
tkm.Button(ventana, text="Lista Doblemente Enlazada", command=ActDoble, bg='white', fg='black', borderless=1, relief='flat').place(x=450, y=120)
tkm.Button(ventana, text="Lista Indexada", command=ActIndex, bg='white', fg='black', borderless=1, relief='flat').place(x=660, y=120)

ventana.mainloop()