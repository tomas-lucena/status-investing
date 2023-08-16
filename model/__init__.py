from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

def init_model():
    db_engine = create_engine("postgresql://postgres:statusinvesting@localhost:5433/postgres")

    from model.dados_cadastrais import DadosCadastrais
    from model.indicador_anual import IndicadorAnual
    from model.indicador_trimestral import IndicadorTrimestral

    Base.metadata.create_all(db_engine, Base.metadata.tables.values(),checkfirst=True)


