from .conexion import ConexionDB
from tkinter import messagebox

# def crearVuelo(origen, destino, horario, precio, id_asientos):
#     con = ConexionDB()
#     try:
#         con.cursor.execute("INSERT INTO Vuelos_tbl (origenV, destinoV, horarioV, precioV, idAsientos) VALUES (?, ?, ?, ?, ?)", (origen, destino, horario, precio, id_asientos))
#         jshg= con.cursor.execute("SELECT MAX(numeroVuelo) FROM Vuelos_tbl").fetchone()
#         if jshg and jshg['origenV'] == origen and jshg['destinoV'] == destino and jshg['horarioV'] == horario and jshg['precioV'] == precio and jshg['idAsientos'] == id_asientos:
#             con.cursor.execute("INSERT INTO Asientos_tbl (puestosTotalesV, puestosDisponiblesV, numeroVuelo)) VALUES (?, ?, ?)", (40, 40, jshg[0]))
#             con.conexion.commit()
#             con.closeConexion()
#             return True
#         else:
#             con.conexion.rollback()
#             ti = 'Error al crear el vuelo'
#             tex = 'El vuelo ya existe en este momento en la base de datos'
#             messagebox.showerror(ti, tex)
#             return False
#     except:
#         con.conexion.rollback()
#         ti = 'Error al crear el vuelo'
#         tex = 'No se pudo crear el vuelo en este momento en la base de datos'
#         messagebox.showerror(ti, tex)
#         return False

def crearVuelo(origen, destino, horario, precio, id_asientos):
    con = ConexionDB()
    
    try:
        con.cursor.execute("INSERT INTO Vuelos_tbl (origenV, destinoV, horarioV, precioV, idAsientos) VALUES (?, ?, ?, ?, ?)",
                           (origen, destino, horario, precio, id_asientos))
        
        jshg = con.cursor.execute("SELECT MAX(numeroVuelo) FROM Vuelos_tbl").fetchone()[0]
        
        con.cursor.execute("INSERT INTO Asientos_tbl (puestosTotalesV, puestosDisponiblesV, numeroVuelo) VALUES (?, ?, ?)",
                           (40, 40, jshg))
        
        con.closeConexion()
        return True

    except :
        con.conexion.rollback()
        ti = 'Error al crear el vuelo'
        tex = 'No se pudo crear el vuelo en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False




def modificarVuelo(numerovuelo, origen, destino, horario, precio, id_asientos):
    con = ConexionDB()
    try:
        con.cursor.execute("UPDATE Vuelos_tbl SET origenV = ?, destinoV = ?, horarioV = ?, precioV = ?, idAsientos = ? WHERE numeroVuelo = ?", (origen, destino, horario, precio, id_asientos, numerovuelo))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al modificar el vuelo'
        tex = 'No se pudo modificar el vuelo en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def eliminarVuelo(numerovuelo):
    con = ConexionDB()
    try:
        con.cursor.execute("DELETE FROM Vuelos_tbl WHERE numeroVuelo = ?", (numerovuelo))
        con.cursor.execute("DELETE FROM Asientos_tbl WHERE idAsientos = ?", (numerovuelo))
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al eliminar el vuelo'
        tex = 'No se pudo eliminar el vuelo en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def mostrarVuelos():
    con = ConexionDB()
    sql = """SELECT * FROM Vuelos_tbl"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return listo

def filtrarVuelos(origen, destino, fecha):
    con = ConexionDB()
    sql = f"""SELECT * FROM Vuelos_tbl WHERE origenV = '{origen}' OR destinoV = '{destino}' OR horarioV ='{fecha}' """
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'No se pudieron filtrar los vuelos en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return listo

def crearUsuario(nombre, email, telefono):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO Usuarios_tbl (nombreUs, emailUs, telefonoUs) VALUES (?, ?, ?)", (nombre, telefono, email))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Usuario'
        tex = 'No se pudo crear el Usuario en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def modificarUsuarios(nombre, telefono, email, id_usuario):
    con = ConexionDB()
    try:
        con.cursor.execute("UPDATE Usuarios_tbl SET nombreUs = ?, emailUs = ?, telefonoUs = ? WHERE idUsuario = ?", (nombre, email, telefono, id_usuario))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al modificar el usuario'
        tex = 'No se pudo modificar el usuario en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def eliminarUsuario(id_usuario):
    con = ConexionDB()
    try:
        con.cursor.execute("DELETE FROM Usuarios_tbl WHERE idUsuario = ?", (id_usuario))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al eliminar el usuario'
        tex = 'No se pudo eliminar el usuario en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def mostrarUsuarios():
    con = ConexionDB()
    sql = """SELECT * FROM Usuarios_tbl"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Usuarios no es accesible en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return listo

def mostrarAsientos(silla):
    con = ConexionDB()
    sql = "SELECT * FROM Asientos_tbl WHERE numeroVuelo = ?"
    listo = []

    try:
        listo = con.cursor.execute(sql, (silla,)).fetchall()  # Pasamos el valor de silla como argumento separado
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Asientos no es accesible en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return listo

def crearReserva(id_usuario, numerovuelo, numerosilla, puestosdisponibles):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO Reservas_tbl (idUsuario, numeroVuelo, numeroSilla, Estado) VALUES (?, ?, ?, 'Reservado')", (id_usuario, numerovuelo, numerosilla))
        con.cursor.execute("UPDATE Asientos_tbl SET puestosDisponiblesV = ? WHERE numeroVuelo = ?", (puestosdisponibles, numerovuelo))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al realizar la reserva'
        tex = 'No se pudo realizar la reserva en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def modificarReserva(idreserva, numerosilla):
    con = ConexionDB()
    try:
        con.cursor.execute("UPDATE Reservas_tbl SET numeroSilla = ? WHERE idReserva = ?", (numerosilla, idreserva))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al modificar la reserva'
        tex = 'No se pudo modificar la reserva en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def eliminarReserva(id_reserva):
    con = ConexionDB()
    try:
        con.cursor.execute("DELETE FROM Reservas_tbl WHERE idReserva = ?", (id_reserva,))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al cancelar la reserva'
        tex = 'No se pudo cancelar la reserva en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False
    
def actualizarPuestosDisponibles(puestos_disponibles,numero_vuelo):
    con = ConexionDB()
    try:
        con.cursor.execute("UPDATE Asientos_tbl SET puestosDisponiblesV = ? WHERE numeroVuelo =?", (puestos_disponibles,numero_vuelo ))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Erroren al modicar el asiento'
        tex = 'No se pudomodificar el asiento en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def mostrarReserva():
    con = ConexionDB()
    sql = """SELECT * FROM Reservas_tbl"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Usuarios no es accesible en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return listo
 
def crearLista(idusuario, numerovuelo):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO ListaEspera_tbl (idUsuario, numeroVuelo) VALUES (?, ?)", (idusuario, numerovuelo))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al unirse a la lista de espera'
        tex = 'No se pudo unirse a la lista de espera en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False
    
def modificarLista(idlistaesp, numerovuelo, idusuario):
    con = ConexionDB()
    try:
        con.cursor.execute("UPDATE ListaEspera_tbl SET numeroVuelo = ?, idUsuario = ? WHERE idListaEspera = ?", (numerovuelo, idusuario, idlistaesp))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al modificar el registro de la lista de espera'
        tex = 'No se pudo modificar el registro de la lista de espera en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def eliminarLista(idlistaesp):
    con = ConexionDB()
    try:
        con.cursor.execute("DELETE FROM ListaEspera_tbl WHERE idRegistro = ?", (idlistaesp,))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al eliminar el registro de la lista de espera'
        tex = 'No se pudo eliminar el registro de la lista de espera en este momento en la base de datos'
        messagebox.showerror(ti, tex)
        return False

def mostrarListaEspera():
    con = ConexionDB()
    sql = """SELECT * FROM ListaEspera_tbl"""
    lista_registros = []
    try:
        lista_registros = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla de Lista de Espera no es accesible en este momento en la base de datos'
        messagebox.showerror(ti, tex)
    return lista_registros
