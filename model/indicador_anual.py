from sqlalchemy import Date,Column,Float,DateTime,String, Integer
from sqlalchemy.ext.declarative import declarative_base
from model import Base

class IndicadorAnual(Base):
    __tablename__ = 't_indicador_anual'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Integer)
    categoria = Column(String)
    ativo = Column(String)
    indicador = Column(String)
    valor = Column(Float)