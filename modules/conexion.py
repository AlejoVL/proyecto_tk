import sqlite3

class ConexionDB():
    def __init__(self):
        self.DataBase="db/Sistema_Gestion.db"
        self.conexion= sqlite3.connect(self.DataBase)
        self.cursor= self.conexion.cursor()#lo que nos permite acceder a la base de datos, iterara con la base de datos

    def closeConexion(self):
        self.conexion.commit()
        self.conexion.close()