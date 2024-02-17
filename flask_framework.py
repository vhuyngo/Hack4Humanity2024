import flask
import epilepsyTracker
from flask_cors import COR

app = Flask(__name__)
CORS(app, resources={"/": {"origins": "*"}})


@app.route('/')
def epilepsy_check():


