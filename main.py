from scrapper.tickerprice import Tickerprice
from scrapper.indicatorhistoricallist import Indicatorhistoricallist
from scrapper.payoutresult import Payoutresult
from scrapper.fluxocaixa import Fluxocaixa
from scrapper.revenue import Revenue
from scrapper.dre import Dre
from scrapper.passivo import Passivo
from scrapper.ativo import Ativo
from scrapper.dadoscadastrais import Dadoscadastrais
import pandas as pd
import time
from model import init_model

def request_in(cls,lista_ativos):

    s_time = time.time()

    statusInvest = cls()

    responses = [
        (statusInvest.request(ticker),ticker) 
        for ticker in lista_ativos
    ]

    e_time = time.time()

    dados = [
        statusInvest.processa(*res) 
        for res in responses
    ]
    
    df_resultado = pd.concat(dados)
    df_resultado['categoria']= cls.__name__

    print(f"size: {len(df_resultado)} time: {e_time-s_time :.1f}")

    return df_resultado


if __name__ == "__main__":
    init_model()

    statusInvest = Dadoscadastrais()
    resp = statusInvest.request()
    df_dados_cadastrais = statusInvest.processa(resp)
    
    ativos = list(df_dados_cadastrais['ticker'].str.lower())

    df_Indicatorhistoricallist = request_in(Indicatorhistoricallist,ativos)
    df_Payoutresult = request_in(Payoutresult,ativos)
    df_Fluxocaixa = request_in(Fluxocaixa,ativos)
    df_Revenue = request_in(Revenue,ativos)
    df_Dre = request_in(Dre,ativos)
    df_Passivo = request_in(Passivo,ativos)
    df_Ativo = request_in(Ativo,ativos)

    df_indicador_anual = pd.concat([df_Indicatorhistoricallist,df_Payoutresult,df_Fluxocaixa,df_Passivo,df_Ativo])
    df_indicador_trimestral = pd.concat([df_Revenue,df_Dre])

    df_dados_cadastrais.to_sql('t_dados_cadastrais',con='postgresql://postgres:statusinvesting@localhost:5433/postgres',if_exists='replace',index=False)
    df_indicador_anual.to_sql('t_indicador_anual',con='postgresql://postgres:statusinvesting@localhost:5433/postgres',if_exists='replace',index=False)
    df_indicador_trimestral.to_sql('t_indicador_trimestral',con='postgresql://postgres:statusinvesting@localhost:5433/postgres',if_exists='replace',index=False)
    