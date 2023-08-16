from sqlalchemy import Date,Column,Float,DateTime,String, Integer
from sqlalchemy.ext.declarative import declarative_base
from model import Base

class IndicadorTrimestral(Base):
    __tablename__ = 't_indicador_trimestral'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Integer)
    trimestre = Column(Integer)
    categoria = Column(String)
    ativo = Column(String)
    indicador = Column(String)
    valor = Column(Float)

    