###############################################
# Name: Application main
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent))
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

"Eng Gov Bank APIs"

if __name__ == '__main__':
    app.run(port=5000, debug=True)