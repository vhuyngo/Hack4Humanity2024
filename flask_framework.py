from flask import Flask, request, jsonify
from tester.py import open_stream
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, resources={"/epilepsy_check": {"origins": "*"}})


@app.route('/epilepsy_check', methods= ['POST'])
def epilepsy_check():
    try:
        data = request.json
        yt_url = data.get('url')
        # open_stream(yt_url)
        time.sleep(30)
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500
    return jsonify({'timestamps': yt_url})

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)





