###############################################
# Name: banks_uk_events
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from orm.testdb.db import session
from orm.testdb.models.banks_uk import BanksUk

Base = declarative_base()
metadata = Base.metadata

class BanksUkEvent(Base):
    __tablename__ = 'banks_uk_events'

    id = Column(INTEGER, primary_key=True)
    bank_id = Column(ForeignKey(BanksUk.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    tittle = Column(String(128))
    date = Column(String(128))
    notes = Column(String(128))
    bunting = Column(String(128))

    bank = relationship(BanksUk)

    def insertIntoBanksUkEvents(self, bank_id, tittle, date, notes, bunting):
        try:
            row = BanksUkEvent(bank_id=bank_id, tittle=tittle, date=date, notes=notes, bunting=bunting)
            session.add(row)
            session.commit()
            session.close()
            return row.id       

        except Exception as error:  
            print(f"Error in insertIntoBanksUkEvents : {error}")    


    def getEventsForDivision(self, division):     
        try:      
            #result = session.query(BanksUkEvent,BanksUk).filter(BanksUkEvent.id == BanksUk.id).all() 
            result = session.query(BanksUkEvent).join(BanksUk).filter(BanksUk.division == division).all()  
            session.close()     
            return result  

        except Exception as error:  
            print(f"Error in insertIntoBanksUkEvents : {error}")    


if __name__ == '__main__':
    obj = BanksUkEvent()
    r =   obj.getEventsForDivision('test1')   
    for i in r:
        print(i.tittle)    
