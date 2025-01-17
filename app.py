from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Cargar el archivo CSV
bins_data = pd.read_csv("bins.csv", dtype=str)

# Ruta para obtener información de un BIN
@app.route('/bin/<bin_id>', methods=['GET'])
def get_bin_info(bin_id):
    # Filtrar el BIN en el archivo CSV
    result = bins_data[bins_data['number'] == bin_id]
    if not result.empty:
        # Convertir a diccionario y devolver como JSON
        data = result.iloc[0].to_dict()
        return jsonify({"Status": "SUCCESS", "Data": data})
    else:
        return jsonify({"Status": "ERROR", "Message": "BIN not found"}), 404

# Ruta raíz
@app.route('/')
def index():
    return "BIN API is running!"

if __name__ == '__main__':
    app.run(debug=True)
