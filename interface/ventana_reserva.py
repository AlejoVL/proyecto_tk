import tkinter as tk
from tkinter import ttk
from interface.ventana_listaE import Ventana_listaE
from tkinter import messagebox
from modules.consultas import *
from PIL import Image, ImageTk

class Ventana_reservas(tk.Toplevel):
    def __init__(self,detalles, root=None):
        super().__init__(root, width=100, height=100)
        self.title("Reservas")
        self.iconbitmap('.//img//icono2.ico')
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()
        self.tabla_reservas()
        self.listar()
        self.resizable(False, False)
        self.valor_numero_vuelo.set(detalles[0])
        self.entry_vuelo = tk.Entry(self, textvariable=self.valor_numero_vuelo )
        self.valor_numero_silla.set(detalles[5])
        self.entry_silla = tk.Entry(self, textvariable=self.valor_numero_silla )
        # self.valor_numero_silla.set(detallesUsuario[5])
        # self.entry_silla = tk.Entry(self, textvariable=self.valor_numero_silla )

    #Metodo para insertar los campos dentro del Frame
    def campos(self):

        self.id_usuario = tk.Label(self, text= "ID_Usuario")
        self.id_usuario.config(width=20,font=('Arial', 12 ,'bold'))
        self.id_usuario.grid(row=0, column=0, padx=5, pady=5)

        self.numero_vuelo = tk.Label(self, text= "Numero_vuelo")
        self.numero_vuelo.config(width=20,font=('Arial', 12 ,'bold'))
        self.numero_vuelo.grid(row=1, column=0, padx=5, pady=5)

        self.numero_silla = tk.Label(self, text= "Numero_silla")
        self.numero_silla.config(width=20,font=('Arial', 12 ,'bold'))
        self.numero_silla.grid(row=2, column=0, padx=5, pady=5)

        self.valor_id_usuario = tk.StringVar()
        self.entry_usuario = tk.Entry(self, textvariable=self.valor_id_usuario)
        self.entry_usuario.config(width=40)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        self.valor_numero_vuelo = tk.StringVar()
        self.entry_vuelo = tk.Entry(self, textvariable=self.valor_numero_vuelo)
        self.entry_vuelo.config(width=40)
        self.entry_vuelo.grid(row=1, column=1, padx=10, pady=10)

        self.valor_numero_silla = tk.StringVar()
        self.entry_silla = tk.Entry(self, textvariable=self.valor_numero_silla)
        self.entry_silla.config(width=40)
        self.entry_silla.grid(row=2, column=1, padx=10, pady=10)

        self.btn_actualizar = tk.Button(self, text="Agregar a lista de espera")
        self.btn_actualizar.config(width=20, bg="#2B7984", command=self.abrir_quinta_ventana)
        self.btn_actualizar.grid(row=5, column=2, padx=5, pady=5)

        self.btn_reserva = tk.Button(self, text="Reservar")
        self.btn_reserva.config(width=15, bg="#2B7984",command=self.crearReserva1)
        self.btn_reserva.grid(row=3, column=1, padx=5, pady=5)


    #Metodo para insertar la tabla de las reservas
    def tabla_reservas(self):

        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('ID_Reserva','ID_Usuario', 'Numero_Vuelo', 'Numero_silla'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="")
        self.tabla.heading("#1", text="ID_Reserva")
        self.tabla.heading("#2", text="ID_Usuario")
        self.tabla.heading("#3", text="Numero_Vuelo")
        self.tabla.heading("#4", text="Numero_Silla")

        self.tabla.column("#0", width=10)
        self.tabla.column("#1", width=260)
        self.tabla.column("#2", width=260)
        self.tabla.column("#3", width=260)
        self.tabla.column("#4", width=260)
   

        self.btn_actualizar = tk.Button(self, text="Actualizar")
        self.btn_actualizar.config(width=15, bg="#2B7984")
        self.btn_actualizar.grid(row=5, column=0, padx=5, pady=5)

        self.btn_actualizar = tk.Button(self, text="Eliminar")
        self.btn_actualizar.config(width=15, bg="#FF0000", command=self.eliminar)
        self.btn_actualizar.grid(row=5, column=1, padx=5, pady=5)

    #Metodo para abrir el Frame Ventana_listaE
    def abrir_quinta_ventana(self):
        self.quinta_ventana = Ventana_listaE()
        
    def listar(self):
        self.tabla.delete(*self.tabla.get_children())
        datos= mostrarReserva()
        for dato in datos:
         self.tabla.insert('',tk.END ,values=(dato[0],dato[1],dato[2],dato[3]))
        
    
    def crearReserva1(self):
        silla = self.entry_silla.get()  # Obtén el número de silla
        puestos = mostrarAsientos(silla)
        if puestos:
            puesto = puestos[0]  # Consideramos que puestos es una lista de tuplas y tomamos la primera tupla

            if len(puesto) >= 3:
                    puestosd = puesto[2]  # Obten el valor de puestos disponibles del último puesto en la lista

                    if puestosd > 0:  # Verifica que hay puestos disponibles para reservar
                        puestosd -= 1  # Decrementa el número de puestos disponibles
                        print(f"Puestos disponibles después de la reserva: {puestosd}")
                        
                        # Realiza la reserva con el valor actualizado de puestosd
                        exito_reserva = crearReserva(self.entry_usuario.get(), self.entry_vuelo.get(), silla, puestosd)
                        if exito_reserva:
                            self.listar()  # Actualiza la tabla con los datos actualizados
                        else:
                            print("La reserva no se pudo completar")

                    else:
                        messagebox.showerror("Error", "No hay puestos disponibles para reservar")
                        self.quinta_ventana = Ventana_listaE(self.entry_usuario.get(),self.entry_vuelo.get())
                        self.destroy
            else:
                print("La tupla puesto no tiene suficientes elementos")
        else:
            print("No se encontraron puestos disponibles")
            

    def eliminar(self):
        seleccion = self.tabla.selection()
        
        if seleccion:
            item = seleccion[0]
            detalles = self.tabla.item(item, "values")
            response = messagebox.askokcancel("Título", "¿Desea continuar?")
            
            if response:
                id_reserva = detalles[0]
                exito_eliminar = eliminarReserva(id_reserva)
                self.listar()
                
                if exito_eliminar:
                    # Obten el número de silla de la reserva eliminada
                    silla = detalles[3]
                    puestos = mostrarAsientos(silla)
                    
                    if puestos:
                        puesto = puestos[0]
                        puestosd = puesto[2]  # Obten el valor de puestos disponibles del último puesto en la lista
                        puestosd += 1  # Incrementa el número de puestos disponibles
                        
                        # Actualiza la cantidad de asientos disponibles en la base de datos
                        actualizarPuestosDisponibles(puesto[0], puestosd)
                        
                        # Actualiza la tabla con los datos actualizados
                        self.tabla.delete(*self.tabla.get_children())
                        self.listar()
                        print(f"Puestos disponibles después de eliminar la reserva: {puestosd}")
                    else:
                        print("No se encontraron puestos disponibles para la silla especificada")
                        
                else:
                    print("No se pudo eliminar la reserva")
            else:
                print("Seleccionaste 'Cancelar'")


