from flask import Flask
from flask_cors import CORS
import json
app = Flask(__name__)

cors = CORS(app)




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

