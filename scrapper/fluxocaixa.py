from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Fluxocaixa:
    def __init__(self):
        self.endpoint = f"{base_url}getfluxocaixa?"
    
    @retry
    def request(self,ticker,type=0):
        self.data = f"code={ticker.lower()}&type={type}&futureData=false&range.min=2008&range.max=2023&asChart=true"       
        url = f"{self.endpoint}{self.data}"
        
        resp = requests.get(url, headers=headers)
        return resp
    
    def processa(self,resp,ticker=None):
        if resp.status_code != 200:
            print(f"status_code: {resp.status_code}")
            return None
        
        resp_json = resp.json()
        
        if not resp_json['success']:
            return None
        
        resultado = [
            pd.DataFrame(chart['columns'])
                .assign(indicador=chart['item']['key']) 
            for chart in resp_json['data']['chart']
        ]
        
        df_resultado = pd.concat(resultado)
        df_resultado['ativo'] = ticker
        df_resultado = df_resultado.rename(columns=dict(rank="ano",value="valor"))
        df_resultado = df_resultado[['ano','ativo','indicador','valor']]

        return df_resultado
 