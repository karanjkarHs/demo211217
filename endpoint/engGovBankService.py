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
from module.engGovBankMain import loadData, retriveEvents

class EngGovBankService(Resource):
    
    def get(self, division):
        """ Respond with bank details """
        payload = retriveEvents(division)
        return payload , 200 if payload else 404


    def put(self):
        """ Add or update bank deatils"""
        request_data = request.get_json()
        status = loadData(request_data)
        return status , 200 if status else 404