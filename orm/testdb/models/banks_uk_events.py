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

Base = declarative_base()
metadata = Base.metadata

class BanksUkEvent(Base):
    __tablename__ = 'banks_uk_events'

    id = Column(INTEGER, primary_key=True)
    bank_id = Column(ForeignKey('banks_uk.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    tittle = Column(String(128))
    date = Column(DateTime)
    notes = Column(String(128))
    bunting = Column(TINYINT(1))

    bank = relationship('BanksUk')