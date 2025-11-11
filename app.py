from flask import Flask;
from controllers import pila_controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(pila_controller.main, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True) 