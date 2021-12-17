from sys import path
from pathlib import Path 
path.append(str(Path(__file__).resolve().parent.parent.parent))
from pytest import mark
from module.engGovBankMain import loadData, retriveEvents

@mark.bank
class bankDtlsCoreTests:

    # Initial cleanup and data setup
    def prepareEnv():
        pass

    #Test data loading from url
    @mark.load
    @mark.skip
    def test_dataLoading(self):
        result = loadData('https://www.gov.uk/bank-holidays.json')
        if result == "Success":
            assert True
        else:
            assert False    

    #Test data retrival
    @mark.fetch
    #@mark.skip
    def test_dataFetch(self):
        result = retriveEvents('england-and-wales')
        if result:
            assert True
        else:
            assert False 