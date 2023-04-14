from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['PUT'])
def update_data():
    key = request.json['key']
    value = request.json['value']
    data[key] = value
    return jsonify({'message': 'Data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
