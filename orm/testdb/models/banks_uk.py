###############################################
# Name: BanksUk
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from orm.testdb.db import session

Base = declarative_base()
metadata = Base.metadata

class BanksUk(Base):
    __tablename__ = 'banks_uk'

    id = Column(INTEGER, primary_key=True)
    location = Column(String(128))
    division = Column(String(128))

    def insertIntoBanksUk(self, location, division):
        try:
            row = BanksUk(location=location, division=division)
            session.add(row)
            session.commit()
            session.close()
            return row.id

        except Exception as error:  
            print(f"Error in BanksUk.getBankDataFromURL : {error}")

    def getbankLocationId(self, division):
        try:      
            result = session.query(BanksUk).filter(BanksUk.division == division).one()  
            session.close()     
            return result.id  

        except Exception as error:  
            print(f"Error in BanksUk : {error}")                  



if __name__ == '__main__':
    obj = BanksUk()
    r = obj.insertIntoBanksUk('test1','test1')
    print(r)