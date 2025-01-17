import mysql.connector
from mysql.connector import Error
import json

def config_bd():
    try:
        with open('Evidencia 3/config.json', 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'config.json'.") #En caso de este error verificar que la ruta al json sea "Evidencia 3/config" y no la raíz del proyecto.
        return None
    except json.JSONDecodeError:
        print("Error: El archivo 'config.json' está mal formateado.")
        return None

def create_connection():
    config = config_bd()
    if config is None:
        return None
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["usuario"],
            passwd=config["pass"],
            database=config["db"]
        )
    except Error as e:
        print(f"El error '{e}' ocurrió")
    return connection

def execute_query(query, params=None):
    connection = create_connection()
    if connection is None:
        return
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()

def fetch_query(query, params=None):
    connection = create_connection()
    if connection is None:
        return None
    
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
    return result
