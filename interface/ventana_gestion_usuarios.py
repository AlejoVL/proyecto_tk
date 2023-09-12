import tkinter as tk
from tkinter import ttk
from modules.consultas import *
from PIL import Image, ImageTk

class Ventana_usuarios(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root, width=100, height=100)
        self.title("Usuarios")
        self.iconbitmap('.//img//icono2.ico')
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()
        self.tabla_gestion_usuarios()
        self.listar()
        self.resizable(False, False)
        

    #Metodo para insertar los campos dentro del Frame
    def campos(self):

        self.nombre_usuario = tk.Label(self, text= "Nombre")
        self.nombre_usuario.config(width=20,font=('Arial', 12 ,'bold'))
        self.nombre_usuario.grid(row=0, column=0, padx=5, pady=5)

        self.email_usuario = tk.Label(self, text= "Email")
        self.email_usuario.config(width=20,font=('Arial', 12 ,'bold'))
        self.email_usuario.grid(row=1, column=0, padx=5, pady=5)

        self.telefono_usuario = tk.Label(self, text= "Telefono")
        self.telefono_usuario.config(width=20,font=('Arial', 12 ,'bold'))
        self.telefono_usuario.grid(row=2, column=0, padx=5, pady=5)

        self.valor_nombre_usuario = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.valor_nombre_usuario)
        self.entry_nombre.config(width=40)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.valor_email_usuario = tk.StringVar()
        self.entry_email = tk.Entry(self, textvariable=self.valor_email_usuario)
        self.entry_email.config(width=40)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.valor_telefono_usuario = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.valor_telefono_usuario)
        self.entry_telefono.config(width=40)
        self.entry_telefono.grid(row=2, column=1, padx=10, pady=10)

        self.btn_crear = tk.Button(self, text="Crear")
        self.btn_crear.config(width=20, bg="#2B7984", command=self.crearUser)
        self.btn_crear.grid(row=3, column=1, padx=5, pady=5)

        self.btn_actualizar = tk.Button(self, text="Actualizar",command=self.actualizar)
        self.btn_actualizar.config(width=15, bg="#2B7984")
        self.btn_actualizar.grid(row=5, column=0, padx=5, pady=5)

        self.btn_guardar = tk.Button(self, text="Guardar")
        self.btn_guardar.config(width=15, bg="#2B7984" ,command=self.guardar)
        self.btn_guardar.grid(row=5, column=2, padx=5, pady=5)
        
        self.btn_actualizar = tk.Button(self, text="Eliminar")
        self.btn_actualizar.config(width=15, bg="#FF0000" ,command=self.eliminarUser)
        self.btn_actualizar.grid(row=5, column=1, padx=5, pady=5)
        
        
    #Metodo para insertar tabla de gestion de usuarios
    def tabla_gestion_usuarios(self):

        #Espacio para la variable que recorre los registros
        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('ID', 'Nombre', 'Email', 'Telefono'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="")
        self.tabla.heading("#1", text="ID")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Email")
        self.tabla.heading("#4", text="Telefono")
  
        self.tabla.column("#0", width=10)
        self.tabla.column("#1", width=150)
        self.tabla.column("#2", width=150)
        self.tabla.column("#3", width=150)
        self.tabla.column("#4", width=150)
        
    
    def listar(self):
        datos = mostrarUsuarios()
        for dato in datos:
            self.tabla.insert('',tk.END,   values=(dato[0],dato[1], dato[2], dato[3], ))
    
    def crearUser(self):
        self.tabla.delete(*self.tabla.get_children())
        crear = crearUsuario(self.entry_nombre.get(),self.entry_email.get(),self.entry_telefono.get())
        self.listar()
        
    def eliminarUser(self):
        seleccion = self.tabla.selection()
        if seleccion:
                item = seleccion[0]
                detalles = self.tabla.item(item, "values")
                response = messagebox.askokcancel("Título", "¿Desea continuar?")
                if response:
                    self.tabla.delete(*self.tabla.get_children())
                    eliminar = eliminarUsuario(detalles[0])
                    self.listar()
                else:
                    print("Seleccionaste 'Cancelar'")
                
        
    def actualizar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            detalles = self.tabla.item(item, "values")
            
            # Rellenar los campos de entrada con los detalles seleccionados
            self.valor_nombre_usuario.set(detalles[1])  # [1] es el nombre
            self.valor_email_usuario.set(detalles[2])   # [2] es el email
            self.valor_telefono_usuario.set(detalles[3])
            if self.btn_guardar.winfo_ismapped():
                 self.btn_guardar.pack_forget()
            else:
               self.btn_guardar.pack()
    
    def guardar(self):
         # Obtener los valores de los campos de entrada actualizados
        nuevo_nombre = self.valor_nombre_usuario.get()
        nuevo_email = self.valor_email_usuario.get()
        nuevo_telefono = self.valor_telefono_usuario.get()
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            detalles = self.tabla.item(item, "values")
            print(detalles)
            # Obtener el ID del usuario seleccionado
            id_usuario = detalles[0]  # [0] es el ID
            
            # Llamar a la función para actualizar el usuario en la base de datos
            actualizar = modificarUsuarios(nuevo_nombre, nuevo_email, nuevo_telefono, id_usuario)
            
            # Actualizar la tabla
            self.tabla.delete(*self.tabla.get_children())
            self.listar()
