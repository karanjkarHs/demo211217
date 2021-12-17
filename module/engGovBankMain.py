###############################################
# Name: EngGovBankMain
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent))
import requests


class EngGovBankMain():

    def getBankDataFromURL(self):
        """ Gets the bank event details from a given url """
        try:
            pass

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
    