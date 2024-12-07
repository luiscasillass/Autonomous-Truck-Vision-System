import time
import serial
from flask import Flask, jsonify
import mysql.connector
import threading

host_ip = '10.43.49.57'
app = Flask(__name__)
lock = threading.Lock()
dist = -1

# Definir y establecer la conexion a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(
        host=host_ip,
        user='carrito',
        password='cybertruck',
        database='iot'
    )
    return connection

# Obtener los datos de la db
@app.route('/datos', methods=['GET'])
def obtener_datos():
    connection = get_db_connection()
    cursor= connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sensor_data')
    datos= cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(datos)

def saveToDatabase(data):
    try:
        with lock:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = f'UPDATE sensor_data set distance={data}'
            cursor.execute(query)
            connection.commit()
    except mysql.connector.Error as err:
        print(f'Error {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
def startApp():
    app.run(host=host_ip, port=5000)
    
            
