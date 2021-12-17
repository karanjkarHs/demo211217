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

class EngGovBankMain():
    def __init__(self):
        self.bankDetailsJson = {}

    def getBankDataFromURL(self, url):
        """ Gets the bank event details from a given url """
        try:
            response_data = requests.get(url)
            self.bankDetailsJson = json.loads(response_data.text)
            print(response_data.status_code)

        except Exception as error:  
            print(f"Error in EngGovBankMain.getBankDataFromURL : {error}")

    def insertBankDataIntoDb(self):
        """ Insert or update bank details into the db"""
        try:
            pass

        except Exception as error:  
            print(f"Error in EngGovBankMain.insertBankDataIntoDb : {error}")

    def fetchDivisionEvents(self):
        """ Retrive bank details"""
        try:
            pass

        except Exception as error:  
            print(f"Error in EngGovBankMain.fetchDivisionEvents : {error}")
    
def main(url):
    try:
        obj = EngGovBankMain()
        result = obj.getBankDataFromURL(url)
        if result == 200:
            pass
        else:
            print("Error occured in getting the json from url")
            return
            

    except Exception as error:  
        print(f"Error in EngGovBankMain.main : {error}")
    

if __name__ == '__main__':
    obj = EngGovBankMain()
    obj.getBankDataFromURL('https://www.gov.uk/bank-holidays.json')
    print(obj.bankDetailsJson)
