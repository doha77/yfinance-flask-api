from flask import Flask
from .controller import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
