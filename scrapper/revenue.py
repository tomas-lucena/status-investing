from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Revenue:
    def __init__(self):
        self.endpoint = f"{base_url}getrevenue?"
    
    @retry
    def request(self,ticker,type=2):           
        self.data = f"code={ticker.lower()}&type={type}&viewType=1"
        url = f"{self.endpoint}{self.data}"

        resp = requests.get(url, headers=headers)
        return resp
    
    def processa(self,resp,ticker=None):
        if resp.status_code != 200:
            print(f"status_code: {resp.status_code}")
            return None
        
        indicadores = ['receitaLiquida','despesas','lucroLiquido','margemBruta','margemEbitda','margemEbit','margemLiquida']
        
        df = pd.DataFrame(resp.json())
        
        dados = [
            df[['year','quarter',indicador]]
                .rename(columns={indicador:"valor"})
                .assign(indicador=indicador) 
            for indicador in indicadores 
        ]

        df_resultado = pd.concat(dados)
        df_resultado['ativo'] = ticker     
        df_resultado = df_resultado.rename(columns=dict(year="ano",quarter="trimestre",value="valor"))
        df_resultado = df_resultado[['ano','trimestre','ativo','indicador','valor']]

        return df_resultado
