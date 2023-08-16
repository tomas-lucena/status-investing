from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Indicatorhistoricallist:
    def __init__(self):
        self.endpoint = f"{base_url}indicatorhistoricallist"

    @retry
    def request(self,ticker,time=5):           
        self.data = f"codes[]={ticker.lower()}&time={time}&byQuarter=true&futureData=false"

        resp = requests.post(self.endpoint, headers=headers, data=self.data)

        return resp
    
    def processa(self,resp,ticker=None):
        if resp.status_code != 200:
            print(f"status_code: {resp.status_code}")
            return None
        
        resp_json = resp.json()

        if not resp_json.get('success', False):
            print("success == False")
            return None
        
        if ticker is None:
            ticker = list(resp_json['data'].keys())[0]

        resultado = [
            pd.DataFrame(dados['ranks'])
                .assign(indicador=dados['key']) 
            for dados in resp_json['data'][ticker]
        ]

        df_resultado = pd.concat(resultado).assign(ativo=ticker)
        df_resultado = df_resultado.rename(columns=dict(rank="ano",value="valor"))
        df_resultado = df_resultado[['ano','ativo','indicador','valor']]

        return df_resultado
