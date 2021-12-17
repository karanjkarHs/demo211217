###############################################
# Name: EngGovBankMain
# Description : 
#
###############################################
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent.parent.parent))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import database_url

engine = create_engine(database_url,echo = True)

Session = sessionmaker(bind = engine)
session = Session()