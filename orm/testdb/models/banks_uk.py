###############################################
# Name: EngGovBankMain
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

