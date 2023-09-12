import tkinter as tk
from tkinter import ttk
from interface.ventana_gestion_usuarios import Ventana_usuarios
from interface.ventana_reserva import Ventana_reservas
from interface.ventana_listaE import Ventana_listaE
from interface.ventana_password import Ventana_password
from interface.actualizar import actualizar_nuevo
from modules.consultas import *
from PIL import Image, ImageTk

class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=100, height=100)
        self.root = root
        self.pack()
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()
        self.tabla_vuelos()
        self.listar()

    #Metodo para insertar los campos dentro del Frame
    def campos(self):
        #Titulos
        
        self.origen = tk.Label(self, text= "Origen")
        self.origen.config(width=20,font=('Arial', 12 ,'bold'))
        self.origen.grid(row=0, column=0, padx=5, pady=5)

        self.destino = tk.Label(self, text= "Destino")
        self.destino.config(width=20,font=('Arial', 12 ,'bold'))
        self.destino.grid(row=1, column=0, padx=5, pady=5)

        self.fecha = tk.Label(self, text= "Fecha")
        self.fecha.config(width=20,font=('Arial', 12 ,'bold'))
        self.fecha.grid(row=2, column=0, padx=5, pady=5)

        #Campos de entrada
        self.valor_origen = tk.StringVar()
        self.entry_origen = tk.Entry(self, textvariable=self.valor_origen)
        self.entry_origen.config(width=40)
        self.entry_origen.grid(row=0, column=1, padx=10, pady=10)

        self.valor_destino = tk.StringVar()
        self.entry_destino = tk.Entry(self, textvariable=self.valor_destino)
        self.entry_destino.config(width=40)
        self.entry_destino.grid(row=1, column=1, padx=10, pady=10)

        self.valor_fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable=self.valor_fecha)
        self.entry_fecha.config(width=40)
        self.entry_fecha.grid(row=2, column=1, padx=10, pady=10)

        #Botones
        self.btn_nuevo = tk.Button(self, text="Nuevo")
        self.btn_nuevo.config(width=15, bg="#2B7984", command=self.abrir_cuarta_ventana)
        self.btn_nuevo.grid(row=3, column=0, padx=5, pady=5)

        self.btn_filtrar = tk.Button(self, text="Filtrar")
        self.btn_filtrar.config(width=15, bg="#2B7984", command=self.filtrar)
        self.btn_filtrar.grid(row=3, column=1, padx=5, pady=5)

        self.btn_reserva = tk.Button(self, text="Reserva")
        self.btn_reserva.config(width=15, bg="#2B7984", command=self.abrir_segunda_ventana)
        self.btn_reserva.grid(row=0, column=2, padx=5, pady=5)

        self.btn_comprar = tk.Button(self, text="Usuarios")
        self.btn_comprar.config(width=15, bg="#2B7984", command=self.abrir_tercera_ventana)
        self.btn_comprar.grid(row=3, column=2, padx=5, pady=5)

    #Metodo para insertar la tabla de vuelo

    def tabla_vuelos(self):
         #Espacio para la variable que recorre los registros
        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('Numero Vuelo','Origen', 'Destino', 'Fecha/Hora', 'Precio', 'Puestos disponibles'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

      
        self.tabla.heading("#0", text="", anchor="w", command=lambda: None)  # Para eliminar el encabezado vacío
        self.tabla.heading("#1", text="Numero Vuelo", anchor="w")
        self.tabla.heading("#2", text="Origen", anchor="w")
        self.tabla.heading("#3", text="Destino", anchor="w")
        self.tabla.heading("#4", text="Fecha/Hora", anchor="w")
        self.tabla.heading("#5", text="Precio", anchor="w")
        self.tabla.heading("#6", text="Puestos Disponibles", anchor="w")

        self.tabla.column("#0", width=20)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.column("#3", width=100)
        self.tabla.column("#4", width=100)
        self.tabla.column("#5", width=100)
        self.tabla.column("#6", width=100)        

        self.btn_actualizar = tk.Button(self, text="Actualizar")
        self.btn_actualizar.config(width=15, bg="#2B7984",command=self.actualizar)
        self.btn_actualizar.grid(row=5, column=0, padx=5, pady=5)

        self.btn_actualizar = tk.Button(self, text="Eliminar")
        self.btn_actualizar.config(width=15, bg="#FF0000",command=self.eliminar)
        self.btn_actualizar.grid(row=5, column=1, padx=5, pady=5)

        
    
    #interface ventana reserva
    def abrir_segunda_ventana(self):
            seleccion = self.tabla.selection()
            if seleccion:
                item = seleccion[0]
                detalles = self.tabla.item(item, "values")
                self.segunda_ventana = Ventana_reservas(detalles,self.root, )
        
    #interface ventana usuarios
    def abrir_tercera_ventana(self):
        self.tercera_ventana = Ventana_usuarios()

    #interface ventana verificar contraseña
    def abrir_cuarta_ventana(self): 
        self.cuarta_ventana = Ventana_password()

    #interface ventana lista de espera
    def abrir_quinta_ventana(self):
        self.quinta_ventana = Ventana_listaE()
    
    #Metodo para listar los vuelos
    def listar(self):
         datos = mostrarVuelos()        
         for dato in datos:
             self.tabla.insert('',tk.END,  values=(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]))     

    #Metodo para filtrar los vuelos
    def filtrar(self):
        self.tabla.delete(*self.tabla.get_children())
        datos = filtrarVuelos(self.entry_origen.get(), self.entry_destino.get(),self.entry_fecha.get())
        for dato in datos:
             print(dato)
             self.tabla.insert('',tk.END,  values=(dato[0],dato[1], dato[2], dato[3], dato[4], dato[5] ))  
    
    def eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
                item = seleccion[0]
                detalles = self.tabla.item(item, "values")
                print(detalles)
                response = messagebox.askokcancel("Título", "¿Desea continuar?")
                if response:
                    self.tabla.delete(*self.tabla.get_children())
                    eliminarVuelo(detalles[0])
                    self.listar()
                else:
                    print("Seleccionaste 'Cancelar'")
                
    def actualizar(self):
         seleccion = self.tabla.selection()
         if seleccion:
                item = seleccion[0]
                detalles = self.tabla.item(item, "values")
                self.sexta_ventana = actualizar_nuevo(detalles,self.root, )