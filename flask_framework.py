from flask import Flask, request, jsonify
#import epilepsyTracker
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/": {"origins": "*"}})


@app.route('/epilepsy_check', methods= ['POST'])
def epilepsy_check():
    try:
        data = response.json
        yt_url = data.get('url')
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500
    return jsonify({'timestamps': yt_url})

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)





