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

class EngGovBankDataLoad(Resource):

    def put(self):
        """ Add or update bank deatils"""
        request_data = request.get_json()
        url = request_data['url']
        status = loadData(url)
        return status , 200 if status else 404