import mysql.connector
from flask import jsonify
from datetime import date, datetime, time, timedelta

def verification_client(email, password_hash):
    # conexion = mysql.connector.connect(
    #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
    #     user="root",  # Tu nombre de usuario de MySQL
    #     password="root",  # Tu contraseña de MySQL
    #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
    # )

    conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )

    cursor = conexion.cursor()
    # Consulta para verificar si existe un cliente con el nombre, correo y teléfono
    query = "SELECT id_cliente, nombre FROM Cliente WHERE email = %s AND password_hash = %s"
    cursor.execute(query, (email, password_hash))

    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    # my_sql.py

    # Suponiendo que ya tienes el código de conexión a la base de datos y obtención de resultados

    # Devuelve un diccionario en lugar de usar jsonify
    if resultados:
     return {"id": resultados[0]}
    else:
     return {"id": None}
    
def insert_evento_proveedor(id_evento, id_proveedor, estado='Pendiente', justificacion=None):
    try:
        conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )
        cursor = conexion.cursor()

        # Consulta para insertar un nuevo registro en Evento_Proveedor
        query = """
        INSERT INTO Evento_Proveedor (id_evento, id_proveedor, estado, fecha_respuesta, justificacion)
        VALUES (%s, %s, %s, %s, %s)
        """
        fecha_respuesta = datetime.now() if estado != 'Pendiente' else None
        
        cursor.execute(query, (id_evento, id_proveedor, estado, fecha_respuesta, justificacion))
        
        # Confirma la transacción
        conexion.commit()
        return {"success": True, "id_evento_proveedor": cursor.lastrowid}

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"success": False, "error": str(err)}

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
def insert_notification(id_evento, id_usuario, tipo_usuario, mensaje):
    try:
        conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )
        cursor = conexion.cursor()

        # Consulta para insertar un nuevo registro en Evento_Proveedor
        query = """
        INSERT INTO Notificacion (id_evento, id_usuario, tipo_usuario, mensaje)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(query, (id_evento, id_usuario, tipo_usuario, mensaje))
        
        # Confirma la transacción
        conexion.commit()
        return {"success": True,}

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"success": False, "error": str(err)}

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def bring_providers(service):
    # conexion = mysql.connector.connect(
    #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
    #     user="root",  # Tu nombre de usuario de MySQL
    #     password="root",  # Tu contraseña de MySQL
    #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
    # )
    conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )

    cursor = conexion.cursor()
    # Consulta para verificar si existe un cliente con el nombre, correo y teléfono
    query = "SELECT id_proveedor, nombre, servicio, telefono, direccion, email, website FROM Proveedor WHERE servicio = %s"
    cursor.execute(query, (service,))

    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    # my_sql.py

    # Suponiendo que ya tienes el código de conexión a la base de datos y obtención de resultados

    # Devuelve un diccionario en lugar de usar jsonify
    if resultados:
            # Convierte cada tupla en un diccionario y almacénalo en una lista
            proveedores = [
                {
                    "id_proveedor": resultado[0],
                    "nombre": resultado[1],
                    "servicio": resultado[2],
                    "telefono": resultado[3],
                    "direccion": resultado[4],
                    "email": resultado[5],
                    "website": resultado[6]
                }
                for resultado in resultados
            ]
            return {"proveedores": proveedores}
    else:
            return {"proveedores": []}  # Devuelve una lista vacía si no hay coincidencias}}
    
def bring_notifications(id_usuario):
    # conexion = mysql.connector.connect(
    #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
    #     user="root",  # Tu nombre de usuario de MySQL
    #     password="root",  # Tu contraseña de MySQL
    #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
    # )

    conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )
    if isinstance(id_usuario, list):
        id_usuario = id_usuario[0]
    elif isinstance(id_usuario, tuple):
        id_usuario = id_usuario[0]
    cursor = conexion.cursor()

    # Consulta para verificar si existe un cliente con el nombre, correo y teléfono
    query = "SELECT id_notificacion, id_usuario, id_evento, mensaje, fecha FROM Notificacion WHERE id_usuario = %s AND tipo_usuario = 'Cliente'"
    cursor.execute(query, (id_usuario,))

    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    print(id_usuario)

    print(resultados)
    # my_sql.py

    # Suponiendo que ya tienes el código de conexión a la base de datos y obtención de resultados

    # Devuelve un diccionario en lugar de usar jsonify
    #print(resultados)
    if resultados:
            # Convierte cada tupla en un diccionario y almacénalo en una lista
            listaNotificaciones = [
                {
                     "id_notificacion":resultado[0],
                    "id_usuario": resultado[1],
                    "id_evento": resultado[2],
                    "mensaje": resultado[3],
                    "fecha": resultado[4].isoformat(),
                }
                for resultado in resultados
            ]
            return {"listaNotificaciones": listaNotificaciones}
    else:
            return {"listaNotificaciones": []}  # Devuelve una lista vacía si no hay coincidencias

def bring_events_providers(id_evento, id_usuario):
    # conexion = mysql.connector.connect(
    #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
    #     user="root",  # Tu nombre de usuario de MySQL
    #     password="root",  # Tu contraseña de MySQL
    #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
    # )

    conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )
    print(id_usuario)

    if isinstance(id_usuario, list):
        id_usuario = id_usuario[0]
    elif isinstance(id_usuario, tuple):
        id_usuario = id_usuario[0]

    
    cursor = conexion.cursor()
    cursor = conexion.cursor()
    # Consulta para verificar si existe un cliente con el nombre, correo y teléfono
    query = """
    SELECT 
    p.nombre AS nombre_proveedor,   
    p.telefono,
    p.email,
    p.website,
    e.nombre_evento, 
    p.servicio, 
    ep.estado, 
    ep.fecha_respuesta, 
    ep.justificacion
  FROM 
    Evento_Proveedor ep
  JOIN 
    Evento e ON ep.id_evento = e.id_evento
  JOIN  
    Proveedor p ON ep.id_proveedor = p.id_proveedor
  JOIN
    Cliente c ON e.id_cliente = c.id_cliente
  WHERE 
    e.id_cliente = %s 
    AND ep.id_evento = %s;
  """
    cursor.execute(query, (id_usuario, id_evento,))

    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    # my_sql.py

    # Suponiendo que ya tienes el código de conexión a la base de datos y obtención de resultados

    # Devuelve un diccionario en lugar de usar jsonify
    #print(resultados)
    if resultados:
            # Convierte cada tupla en un diccionario y almacénalo en una lista
            listaConexiones = [
                {
                    "nombre_proveedor": resultado[0],
                    "telefono": resultado[1],
                    "email": resultado[2],
                    "website": resultado[3],
                    "nombre_evento": resultado[4],
                    "servicio": resultado[5],
                    "estado": resultado[6],
                    "fecha_respuesta": resultado[7],
                    "justificacion": resultado[8],
                }
                for resultado in resultados
            ]
            return {"listaConexiones": listaConexiones}
    else:
            return {"listaConexiones": []}  # Devuelve una lista vacía si no hay coincidencias

def bring_events(id_cliente):
    # conexion = mysql.connector.connect(
    #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
    #     user="root",  # Tu nombre de usuario de MySQL
    #     password="root",  # Tu contraseña de MySQL
    #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
    # )

    conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )

    if isinstance(id_cliente, list):
        id_cliente = id_cliente[0]
    elif isinstance(id_cliente, tuple):
        id_cliente = id_cliente[0]
    cursor = conexion.cursor()
    # Consulta para verificar si existe un cliente con el nombre, correo y teléfono
    query = "SELECT id_cliente, nombre_evento,fecha_evento,hora_inicio,hora_final,alimentacion,decoracion,transporte,alquiler_lugar,comentarios,asistentes, id_evento FROM Evento WHERE id_cliente = %s"
    cursor.execute(query, (id_cliente,))

    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    # my_sql.py

    # Suponiendo que ya tienes el código de conexión a la base de datos y obtención de resultados

    # Devuelve un diccionario en lugar de usar jsonify
    if resultados:
            #print(resultados)
            # Convierte cada tupla en un diccionario y almacénalo en una lista
            eventos = [
                {
                    "id_cliente": resultado[0],
                    "nombre_evento": resultado[1],
                     "fecha_evento": resultado[2].isoformat() if isinstance(resultado[2], date) else resultado[2],
                     "hora_inicio": str(resultado[3])[:-3] if isinstance(resultado[3], timedelta) else resultado[3],
                     "hora_final":  str(resultado[4])[:-3] if isinstance(resultado[4], timedelta) else resultado[4],
                    "alimentacion": resultado[5],
                    "decoracion": resultado[6],
                    "transporte": resultado[7],
                    "alquiler_lugar": resultado[8],
                     "comentarios": resultado[9],
                     "asistentes": resultado[10],      
                     "id_evento": resultado[11],            
                }
                for resultado in resultados
            ]
            return {"eventos": eventos}
    else:
            return {"eventos": []}  # Devuelve una lista vacía si no hay coincidencias
    
def insert_events(id_cliente, nombre_evento, fecha_evento, hora_inicio, hora_final, alimentacion, decoracion, transporte, alquiler_lugar, comentarios, asistentes):
    try:
        # Conexión a la base de datos
        # conexion = mysql.connector.connect(
        #     host="localhost",  # Cambia esto si tu MySQL está en otro servidor
        #     user="root",  # Tu nombre de usuario de MySQL
        #     password="root",  # Tu contraseña de MySQL
        #     database="GestorEventos"  # El nombre de la base de datos a la que quieres acceder
        # )
        conexion = mysql.connector.connect(
        host="34.71.110.169",  # Cambia esto si tu MySQL está en otro servidor
        user="root",  # Tu nombre de usuario de MySQL
        password="Asmrg*1234",  # Tu contraseña de MySQL
        database="gestoreventos"  # El nombre de la base de datos a la que quieres acceder
    )

        cursor = conexion.cursor()

        # Consulta para insertar un nuevo evento
        query = """
        INSERT INTO Evento (id_cliente, nombre_evento, fecha_evento, hora_inicio, hora_final, alimentacion, decoracion, transporte, alquiler_lugar, comentarios, asistentes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Ejecuta la consulta
        cursor.execute(query, (id_cliente, nombre_evento, fecha_evento, hora_inicio, hora_final, alimentacion, decoracion, transporte, alquiler_lugar, comentarios, asistentes, ))

        # Confirma la transacción
        conexion.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cierra el cursor y la conexión
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
