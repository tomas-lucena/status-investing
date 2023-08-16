from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Passivo:
    def __init__(self):
        self.endpoint = f"{base_url}getbsactivepassivechart?"

    @retry
    def request(self,ticker,type=2):
        self.data = f"code={ticker.lower()}&type={type}"       
        url = f"{self.endpoint}{self.data}"
        resp = requests.get(url, headers=headers)
        return resp
    
    def processa(self,resp,ticker=None):
        if resp.status_code != 200:
            print(f"status_code: {resp.status_code}")
            return None
        
        indicadores = ["ativoTotal","passivoTotal","ativoCirculante","ativoNaoCirculante","passivoCirculante","passivoNaoCirculante","patrimonioLiquido"]
        
        df = pd.DataFrame(resp.json())
        
        dados = [
            df[['year',indicador]]
                .rename(columns={indicador:"valor"})
                .assign(indicador=indicador) 
            for indicador in indicadores 
        ]

        df_resultado = pd.concat(dados)
        df_resultado['ativo'] = ticker     
        df_resultado = df_resultado.rename(columns=dict(year="ano",value="valor"))
        df_resultado = df_resultado[['ano','ativo','indicador','valor']]

        return df_resultado