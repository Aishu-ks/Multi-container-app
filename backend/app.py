from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import time

app = Flask(__name__)
CORS(app)

def connect_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="appdb"
            )
            return conn
        except:
            print("Waiting for DB...")
            time.sleep(2)

@app.route('/')
def home():
    return jsonify({"status": "Backend Running"})

@app.route('/data')
def get_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM greetings LIMIT 1;")
    result = cursor.fetchone()
    conn.close()
    return jsonify({"message": result[0] if result else "No Data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)