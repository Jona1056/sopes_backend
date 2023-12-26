from flask import Flask, jsonify,request
import pyodbc
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS
port = int(os.environ.get('PORT', 5000))
server = 'local-sopes.database.windows.net'
database = 'sopes_db'
username = 'server_db'
password = 'servidor-123'   
driver= '{ODBC Driver 17 for SQL Server}'


@app.route('/', methods=['POST'])
def recibir_datos():
    try:
        # Obtener los datos del formulario enviado por React
        datos_formulario = request.get_json()
        # Extraer el usuario y la contraseña del formulario
        usuario = datos_formulario.get('usuario')
        contrasena = datos_formulario.get('contrasena')
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
          with conn.cursor() as cursor:
            #solo seleccionar la tabla
            cursor.execute("SELECT * FROM Usuarios")
          
            row = cursor.fetchone()
            while row:
              if row[1] == usuario and row[2] == contrasena:
                return jsonify({'message': 'success',
                                'id': row[0],
                                'usuario': row[1],
                                'contrasena': row[2]})
              row = cursor.fetchone()
            return jsonify({'message': 'error', 'error': 'usuario o contraseña incorrecta'})
          
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir
        return jsonify({'error': str(e)})
      


if __name__ == '__main__':
    app.run(debug=True,port=port)