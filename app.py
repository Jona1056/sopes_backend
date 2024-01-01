from flask import Flask, jsonify,request
from flask_cors import CORS
import os
import mysql.connector
app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS
port = int(os.environ.get('PORT', 5000))

config = {
    'user': 'db_sopes',
    'password': 'servidor123',
    'host': '4.157.193.45',
    'database': 'sopes_jonatan',
    'port': 80,
}

@app.route('/', methods=['POST'])
def recibir_datos():
    try:
        datos_formulario = request.get_json()
        usuario = datos_formulario.get('usuario')
        contrasena = datos_formulario.get('contrasena')
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
          if row[1] == usuario and row[2] == contrasena:
            print("usuaario y contrasñea correcta")
            return jsonify({'message': 'success',
                            'id': row[0],
                            'usuario': row[1],
                            'contrasena': row[2]})
        cursor.close()
        conn.close()
        return jsonify({'message': 'error', 'error': 'usuario o contraseña incorrecta'})
          
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
      
@app.route('/crear', methods=['POST'])
def crear_datos():
    try:
        datos_formulario = request.get_json()
        usuario = datos_formulario.get('usuario')
        contrasena = datos_formulario.get('contrasena')
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)"
        cursor.execute(query, (usuario, contrasena))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'success'})
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
    
@app.route('/eliminar', methods=['POST'])
def eliminar_datos():
    try:
        datos_formulario = request.get_json()
        id = datos_formulario.get('usuario')
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        if cursor.rowcount > 0:
            # Se eliminó al menos un registro
            return jsonify({'message': 'success'})
        else:
            # No se eliminó ningún registro con el ID proporcionado
            return jsonify({'message': 'no records deleted'})
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
    
@app.route('/modificar_post', methods=['POST'])
def modificar_post():
    try:
        datos_formulario = request.get_json()
        usuario = datos_formulario.get('usuario2')

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        #obtener datos
        query = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        results = cursor.fetchall()
        for row in results:
          if row[1] == usuario:
            print("usuario encontrado")
            return jsonify({'message': 'success',
                            'id': row[0],
                            'usuario': row[1],
                            'contrasena': row[2]})
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'error', 'error': 'usuario no encontrado'})
        
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
    
@app.route('/modificar_get', methods=['POST'])
def modificar_get():
    try:
        datos_formulario = request.get_json()

        usuario = datos_formulario.get('usuario')
        contrasena = datos_formulario.get('contrasena')
        usuario2 = datos_formulario.get('usuario2')
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "UPDATE usuarios SET usuario = %s, contrasena = %s WHERE usuario = %s"
        cursor.execute(query, (usuario, contrasena,usuario2))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'success'})
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
    
@app.route('/buscar', methods=['POST'])
def buscar():
    try:
        datos_formulario = request.get_json()
        usuario = datos_formulario.get('usuario2')

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        #obtener datos
        query = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        results = cursor.fetchall()
        for row in results:
          if row[1] == usuario:
            print("usuario encontrado")
            return jsonify({'message': 'success',
                            'id': row[0],
                            'usuario': row[1],
                            'contrasena': row[2]})
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'error', 'error': 'usuario no encontrado'})
        
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True,port=port,host='0.0.0.0')