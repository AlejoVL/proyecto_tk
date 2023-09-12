import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modules.consultas import *

class actualizar_nuevo(tk.Toplevel):
    def __init__(self,detalles, root=None):
        super().__init__(root, width=100, height=100)
        self.title("Nuevo vuelo")
        self.iconbitmap('.//img//icono2.ico')
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()
        self.tabla_crear()
        self.listar()
        self.nv = detalles[0]
        self.valor_origen_vuelo.set(detalles[1])
        self.entry_origen = tk.Entry(self, textvariable=self.valor_origen_vuelo )
        
        self.valor_destino_vuelo.set(detalles[2])
        self.entry_destino = tk.Entry(self, textvariable=self.valor_destino_vuelo )
        
        self.valor_horario_vuelo.set(detalles[3])
        self.entry_horario = tk.Entry(self, textvariable=self.valor_horario_vuelo)
        
        self.valor_precio_vuelo.set(detalles[3])
        self.entry_precio = tk.Entry(self, textvariable=self.valor_precio_vuelo)
        
        self.valor_id_asiento.set(detalles[3])
        self.entry_asiento = tk.Entry(self, textvariable=self.valor_id_asiento)

    #Metodo para insertar los campos dentro del Frame
    def campos(self):

        #Campos de titulo
        self.origen_vuelo = tk.Label(self, text= "Origen")
        self.origen_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.origen_vuelo.grid(row=0, column=0, padx=5, pady=5)

        self.destino_vuelo = tk.Label(self, text= "Destino")
        self.destino_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.destino_vuelo.grid(row=1, column=0, padx=5, pady=5)

        self.horario_vuelo = tk.Label(self, text= "Horario")
        self.horario_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.horario_vuelo.grid(row=2, column=0, padx=5, pady=5)

        self.precio_vuelo = tk.Label(self, text= "Precio")
        self.precio_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.precio_vuelo.grid(row=3, column=0, padx=5, pady=5)

        self.id_asiento_vuelo = tk.Label(self, text= "ID_asientos")
        self.id_asiento_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.id_asiento_vuelo.grid(row=4, column=0, padx=5, pady=5)

        #Campos de texto
        self.valor_origen_vuelo = tk.StringVar()
        self.entry_origen = tk.Entry(self, textvariable=self.valor_origen_vuelo)
        self.entry_origen.config(width=40)
        self.entry_origen.grid(row=0, column=1, padx=10, pady=10)

        self.valor_destino_vuelo = tk.StringVar()
        self.entry_destino = tk.Entry(self, textvariable=self.valor_destino_vuelo)
        self.entry_destino.config(width=40)
        self.entry_destino.grid(row=1, column=1, padx=10, pady=10)

        self.valor_horario_vuelo = tk.StringVar()
        self.entry_horario = tk.Entry(self, textvariable=self.valor_horario_vuelo)
        self.entry_horario.config(width=40)
        self.entry_horario.grid(row=2, column=1, padx=10, pady=10)

        self.valor_precio_vuelo = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.valor_precio_vuelo)
        self.entry_precio.config(width=40)
        self.entry_precio.grid(row=3, column=1, padx=10, pady=10)

        self.valor_id_asiento = tk.StringVar()
        self.entry_asiento = tk.Entry(self, textvariable=self.valor_id_asiento)
        self.entry_asiento.config(width=40)
        self.entry_asiento.grid(row=4, column=1, padx=10, pady=10)

        self.btn_crear = tk.Button(self, text="Guardar")
        self.btn_crear.config(width=15, bg="#2B7984", command=self.guardar)
        self.btn_crear.grid(row=5, column=1, padx=5, pady=5)

    #Metodo para insertar la tabla de crear vuelo
    def tabla_crear(self):

        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=( 'Numero Vuelo','Origen', 'Destino', 'Fecha/Hora', 'Precio', 'ID Asientos'))
        self.tabla.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=6, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

       
        self.tabla.heading("#0", text="")
        self.tabla.heading("#1", text="Numero Vuelo")
        self.tabla.heading("#2", text="Origen")
        self.tabla.heading("#3", text="Destino")
        self.tabla.heading("#4", text="Fecha/Hora")
        self.tabla.heading("#5", text="Precio")
        self.tabla.heading("#6", text="ID Asientos")

        self.tabla.column("#0", width=20)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.column("#3", width=100)
        self.tabla.column("#4", width=100)
        self.tabla.column("#5", width=100)
        self.tabla.column("#6", width=100)   
        
        
    def guardar(self):
        nuevo_origen = self.entry_origen.get()
        nuevo_destino = self.entry_destino.get()
        nuevo_horario = self.entry_horario.get()
        nuevo_precio = self.entry_precio.get()
        nuevo_asiento = self.entry_asiento.get()
        self.tabla.delete(*self.tabla.get_children())
        crear = modificarVuelo(self.nv,nuevo_origen,nuevo_destino,nuevo_horario,nuevo_precio,nuevo_asiento)
        self.listar()
        
    #Metodo para listar los vuelos
    def listar(self):
         datos = mostrarVuelos()        
         for dato in datos:
             self.tabla.insert('',tk.END,  values=(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]))  
    
 