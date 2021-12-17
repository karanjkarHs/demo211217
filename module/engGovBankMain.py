###############################################
# Name: EngGovBankMain
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent))
import requests
import json
from orm.testdb.models.banks_uk_events import banksUkEvent
from orm.testdb.models.banks_uk import banksUk
from datetime import datetime
from collections import OrderedDict

class EngGovBankMain():
    def __init__(self):
        self.bankDetailsJson = {}

    def getBankDataFromURL(self, url):
        """ Gets the bank event details from a given url """
        try:
            response_data = requests.get(url)
            self.bankDetailsJson = json.loads(response_data.text)
            return response_data.status_code

        except Exception as error:  
            print(f"Error in EngGovBankMain.getBankDataFromURL : {error}")

    def insertBankEventsDataIntoDb(self, division):
        """ Insert or update bank details into the db"""
        try:
            bankDivId = banksUk.getbankLocationId(division)
            england_and_wales = self.bankDetailsJson.get(division).get("events")
            for events in england_and_wales:
                title = events.get("title")
                date = events.get("date")
                notes = events.get("notes")
                bunting = events.get("bunting")
                banksUkEvent.insertIntoBanksUkEvents(bankDivId, title, date, notes, bunting)
            return    

        except Exception as error:  
            print(f"Error in EngGovBankMain.insertBankEventsDataIntoDb : {error}")

    def insertBankDataIntoDb(self):
        """ Insert or update bank details into the db"""
        try:
            # for england-and-wales
            self.insertBankEventsDataIntoDb("england-and-wales")
            # for scotland
            self.insertBankEventsDataIntoDb("scotland")
            # for northern-ireland
            self.insertBankEventsDataIntoDb("northern-ireland")                                   
            return "Success"    

        except Exception as error:  
            print(f"Error in EngGovBankMain.insertBankDataIntoDb : {error}")

    def fetchDivisionEvents(self, division):
        """ Retrive bank details"""
        try:
            result = banksUkEvent.getEventsForDivision(division)
            events = []
            for event in result:
                rowData = OrderedDict()
                rowData["title"] = event.tittle
                rowData["date"] = event.date
                rowData["notes"] = event.notes
                if event.bunting == "1":
                    rowData["bunting"] = True
                elif event.bunting == "0":
                    rowData["bunting"] = False    
                events.append(rowData)

            return events    

        except Exception as error:  
            print(f"Error in EngGovBankMain.fetchDivisionEvents : {error}")
    
def loadData(url):
    try:
        obj = EngGovBankMain()
        result = obj.getBankDataFromURL(url)
        if result == 200:
            pass
        else:
            print("Error occured in getting the json from url")
            return
        result = obj.insertBankDataIntoDb()   
        return result 


    except Exception as error:  
        print(f"Error in EngGovBankMain.main : {error}")
    
def retriveEvents(division):
    try:
        obj = EngGovBankMain()
        result = obj.fetchDivisionEvents(division)
        return result

    except Exception as error:  
        print(f"Error in EngGovBankMain.main : {error}")



if __name__ == '__main__':
    #obj = EngGovBankMain()
    #obj.getBankDataFromURL('https://www.gov.uk/bank-holidays.json')
    #print(obj.bankDetailsJson)
    #loadData('https://www.gov.uk/bank-holidays.json')
    r = retriveEvents('england-and-wales')
    print(json.dumps(r))

