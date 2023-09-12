import tkinter as tk
from tkinter import messagebox
from interface.ventana_nuevo import Ventana_nuevo
from PIL import Image, ImageTk

class Ventana_password(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root, width=100, height=100)
        self.title("Contraseña")
        self.iconbitmap('.//img//icono2.ico')
        self.background_image = Image.open(".//img//gradiente.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.campos()

    def campos(self):

        #Campo de titulo
        self.password = tk.Label(self, text= "Ingresa la contraseña")
        self.password.config(width=20,font=('Arial', 12 ,'bold'))
        self.password.grid(row=0, column=0, padx=5, pady=5)

        #Campo de entrada de texto
        self.valor_password = tk.StringVar()
        self.entry_password = tk.Entry(self, textvariable=self.valor_password)
        self.entry_password.config(width=40)
        self.entry_password.grid(row=1, column=0, padx=10, pady=10)

        self.btn_verificar = tk.Button(self, text="Verificar")
        self.btn_verificar.config(width=15, bg="#2B7984", command=self.verificar)
        self.btn_verificar.grid(row=2, column=0, padx=5, pady=5)

    def verificar(self):
        print(self.valor_password.get())
        if self.valor_password.get() == "12345":
            messagebox.askokcancel("Ingreso", "Bienvenido al sistema")
            Ventana_nuevo()        
        else:
            self.btn_verificar.grid(row=2, column=0, padx=5, pady=5)
            self.btn_verificar = tk.Button(self, text="cambio")
            self.btn_verificar.config(width=15, bg="#2B7984", command=self.imprimir)
            self.error = tk.Label(self, text= "Contraseña Incorrecta!")
            self.error.config(width=20,font=('Arial', 12 ,'bold'), bg="red")
            self.error.grid(row=4, column=0, padx=5, pady=5)
def imprimir():
        print('funciona')