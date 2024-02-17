from flask import Flask, request, jsonify
import epilepsyTracker
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/": {"origins": "*"}})


@app.route('/epilepsy_check', methods= ['GET'])
def epilepsy_check():
    try:
        data = response.json
        URL = data.get('url')
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500
    




