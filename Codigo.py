from flask import Flask, jsonify, request
from my_sql import bring_events, bring_events_providers, bring_notifications, bring_providers, insert_evento_proveedor, insert_events, insert_notification, verification_client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route('/')
def home():
    return jsonify({"message": "¡Bienvenido a la API!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password_hash = data.get('password_hash')

    response = verification_client(email, password_hash)

    # Usa jsonify en la respuesta de Flask, no en la función verification_client
    #print(response["id"])
    if response["id"] != 0 and response and response["id"] != None:
        return jsonify({
            "id": response["id"],
            "name": response["id"][1],
        })
    else:
        return jsonify({"id": 0}), 401
    
@app.route('/providers', methods=['POST'])
def provider():
    data = request.get_json()
    service = data.get('service')

    response = bring_providers(service)

    # Verifica si la lista de proveedores no está vacía
    if response["proveedores"]:
        return jsonify(response)
    else:
        return jsonify({"proveedores": []}), 404  # 404 si no se encuentran proveedores
    

# Otras rutas de tu API...

@app.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    
    # Extrae los datos del JSON recibido
    print(data.get("id_cliente"), data.get("nombre_evento"),"--", data.get("fecha_evento"), "--", data.get("hora_inicio"), "--",data.get("hora_final"),data.get("alimentacion"), data.get("decoracion"), data.get("transporte"), data.get("alquiler_lugar"), data.get("comentarios"), data.get("asistentes"))
    id_cliente = data.get("id_cliente")
    nombre_evento = data.get("nombre_evento")
    fecha_evento = data.get("fecha_evento")
    hora_inicio = data.get("hora_inicio")
    hora_final = data.get("hora_final")
    alimentacion = data.get("alimentacion")
    decoracion = data.get("decoracion")
    transporte = data.get("transporte")
    alquiler_lugar = data.get("alquiler_lugar")
    comentarios = data.get("comentarios")
    asistentes = data.get("asistentes")
    
    # # Llama a la función insert_events y almacena la respuesta
    # response = insert_events(
    #     id_cliente[0], nombre_evento, fecha_evento, hora_inicio, hora_final,
    #     alimentacion, decoracion, transporte, alquiler_lugar, comentarios, asistentes
    # )
    
    if isinstance(id_cliente, list) or isinstance(id_cliente, tuple):
        id_cliente = id_cliente[0]  # Accede al primer elemento si es una lista o tupla

    try:
        # Llama a la función insert_events con los datos
        response = insert_events(
            id_cliente, nombre_evento, fecha_evento, hora_inicio, hora_final,
            alimentacion, decoracion, transporte, alquiler_lugar, comentarios, asistentes
        )
        return jsonify({"message": "Evento agregado exitosamente."}), 201  # 201 para creación exitosa
    except: 
        return jsonify({"message": "Error al agregar el evento."}), 500  # 500 para error interno del servidor
         # Si llega aquí, la inserción fue exitosa
@app.route('/showEvents', methods=['POST'])
def events():
  try:
    data = request.get_json()
    service = data.get('userId')

    response = bring_events(service)

    # Verifica si la lista de proveedores no está vacía
    if response["eventos"]:
        return jsonify(response)
    else:
        return jsonify({"eventos": []}), 404  # 404 si no se encuentran proveedores
  except Exception as e:
        # Registra el error y devuelve un mensaje de error
        print(f"Error en /showEvents: {e}")
        return jsonify({"error": "Se produjo un error al procesar la solicitud."}), 500

@app.route('/showEventProvider', methods=['POST'])
def event_provider():
  try:
    data = request.get_json()
    id_evento = data.get('id_evento')
    id_usuario = data.get("userId")
    print(id_usuario)

    response = bring_events_providers(id_evento, id_usuario)

    # Verifica si la lista de proveedores no está vacía
    print(response)
    if response["listaConexiones"]:
        return jsonify(response)
    else:
        return jsonify({"listaConexiones": []}), 404  # 404 si no se encuentran proveedores
  except Exception as e:
        # Registra el error y devuelve un mensaje de error
        print(f"Error en /showEventProvider: {e}")
        return jsonify({"error": "Se produjo un error al procesar la solicitud."}), 500  
  
@app.route('/get_notifications', methods=['POST'])
def getNotifications():
  try:
    data = request.get_json()
    id_usuario = data.get('userId')

    response = bring_notifications(id_usuario)

    if id_usuario == None:
      return jsonify({"listaNotificaciones": []}),404
    # Verifica si la lista de proveedores no está vacía
    print(response)
    if response["listaNotificaciones"]:
        return jsonify(response)
    else:
        return jsonify({"listaNotificaciones": []}), 404  # 404 si no se encuentran proveedores
  except Exception as e:
        # Registra el error y devuelve un mensaje de error
        print(f"Error en /get_notifications: {e}")
        return jsonify({"error": "Se produjo un error al procesar la solicitud."}), 500  

@app.route('/evento_proveedor', methods=['POST'])
def add_evento_proveedor():
    data = request.get_json()
    id_evento = data.get('id_evento')
    id_proveedor = data.get('id_proveedor')
    estado = data.get('estado', 'Pendiente')  # Valor por defecto
    justificacion = data.get('justificacion', None)

    # Llama a la función de inserción
    response = insert_evento_proveedor(id_evento, id_proveedor, estado, justificacion)

    # Responde según el resultado de la inserción
    if response["success"]:
        return jsonify({"message": "Registro creado exitosamente", "id_evento_proveedor": response["id_evento_proveedor"]}), 201
    else:
        return jsonify({"error": response["error"]}), 400    
    
@app.route('/add_notification', methods=['POST'])
def add_notification():
    data = request.get_json()
    id_evento = data.get('id_evento')
    id_usuario = data.get('id_usuario')
    tipo_usuario = data.get('tipo_usuario', 'Proveedor')  # Valor por defecto
    mensaje = data.get('mensaje')

    # Llama a la función de inserción
    response = insert_notification(id_evento, id_usuario, tipo_usuario, mensaje)

    # Responde según el resultado de la inserción
    if response["success"]:
        return jsonify({"message": "Registro creado exitosamente"}), 201
    else:
        return jsonify({"error": response["error"]}), 400    
    
if __name__ == '__main__':
    # Prueba independiente de verification_client
    #print(verification_client("Carlos Pérez", "carlos.perez@example.com", "1234567890"))
    #print(verification_client("Ana Gómez", "ana.gomez@example.com", "0987654321"))
    print(bring_providers("Alimentación"))
    #print(insert_events(1,'Cumpleaños de Carlos', '2024-11-15', '15:00', '19:00', '50 hamburguesas, 20 refrescos', 'Globos rojos y azules', '2 autobuses', 'Alquiler del salón fiesta', 'El cliente pidió agregar menú vegetariano', 50))
    app.run(debug=True)


