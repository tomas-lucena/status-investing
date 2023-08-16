from sqlalchemy import Date,Column,Float,DateTime,String, Integer
from sqlalchemy.ext.declarative import declarative_base
from model import Base

class DadosCadastrais(Base):
    __tablename__ = 't_dados_cadastrais'

    companyid = Column(Integer,primary_key=True)
    ticker = Column(String)
    companyname = Column(String)
    subsectorname = Column(String)
    segmentname = Column(String)
    sectorname = Column(String)