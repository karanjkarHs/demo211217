###############################################
# Name: EngGovBankService
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent))
from flask_restful import Resource
from flask import request

class EngGovBankService(Resource):
    
    def get(self):
        """ Respond with bank details """
        pass

    def put(self):
        """ Add or update bank deatils"""
        pass