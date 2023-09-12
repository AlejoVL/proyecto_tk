import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modules.consultas import *


class Ventana_listaE(tk.Toplevel):
    def __init__(self,dato1,dato2, root=None):
        super().__init__(root, width=100, height=100)
        self.title("Lista de espera")
        self.iconbitmap('.//img//icono2.ico')
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()
        self.tabla_espera()
        self.listar()
        # self.eliminar()
        self.valor_id_usuario.set(dato1)
        self.entry_id_usuario = tk.Entry(self, textvariable=self.valor_id_usuario )
        
        self.valor_numero_vuelo.set(dato2)
        self.entry_numero_vuelo = tk.Entry(self, textvariable=self.valor_numero_vuelo )

    #Metodo para insertar los campos dentro del Frame
    def campos(self):

        #Campo de titulo
        self.numero_vuelo = tk.Label(self, text= "Numero de vuelo")
        self.numero_vuelo.config(width=25,font=('Arial', 12 ,'bold'))
        self.numero_vuelo.grid(row=1, column=0, padx=5, pady=5)

        self.id_usuario = tk.Label(self, text= "ID usuario")
        self.id_usuario.config(width=25,font=('Arial', 12 ,'bold'))
        self.id_usuario.grid(row=2, column=0, padx=5, pady=5)

        #Campos de texto

        self.valor_numero_vuelo = tk.StringVar()
        self.entry_numero_vuelo = tk.Entry(self, textvariable=self.valor_numero_vuelo)
        self.entry_numero_vuelo.config(width=40)
        self.entry_numero_vuelo.grid(row=1, column=1, padx=10, pady=10)
        
        self.valor_id_usuario = tk.StringVar()
        self.entry_id_usuario = tk.Entry(self, textvariable=self.valor_id_usuario)
        self.entry_id_usuario.config(width=40)
        self.entry_id_usuario.grid(row=2, column=1, padx=10, pady=10)

        #Botones
        self.btn_crear = tk.Button(self, text="Crear")
        self.btn_crear.config(width=15, bg="#2B7984" ,command=self.crearLEspera)
        self.btn_crear.grid(row=3, column=1, padx=5, pady=5)

    #Metodo para insertar la tabla de lista de espera
    def tabla_espera(self):

        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('ID_lista_espera','Numero_vuelo', 'ID_usuario'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="")
        self.tabla.heading("#1", text="ID_lista_espera")
        self.tabla.heading("#2", text="Numero_Vuelo")
        self.tabla.heading("#3", text="ID_usuario")
        
        self.tabla.column("#0", width=20)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.column("#3", width=100)

        # self.btn_crear = tk.Button(self, text="Eliminar")
        # self.btn_crear.config(width=15, bg="#2B7984")
        # self.btn_crear.grid(row=5, column=1, padx=5, pady=5)
     
    def crearLEspera(self):
        hola = crearLista(self.entry_id_usuario.get(),self.entry_numero_vuelo.get())
        if hola:
            print('reserva en lista de espera correctamente')
        else:
             print('error en lista de espera')
             
    # def eliminar(self):
    #     asientos = mostrarAsientos(self.entry_numero_vuelo.get())
    #     cantidad_asientos = len(asientos)
    #     print(cantidad_asientos)
    #     nV = []

        
        
    
    def listar(self):
         datos = mostrarListaEspera()        
         for dato in datos:
             self.tabla.insert('',tk.END,  values=(dato[0], dato[1], dato[2]))     
