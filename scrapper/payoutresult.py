from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Payoutresult:
    def __init__(self):
        self.endpoint = f"{base_url}payoutresult?"
    
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
        
        resp_json = resp.json()

        if not resp_json.get('chart', False):
            return None
        
        series = resp_json['chart']['series']
        anos = resp_json['chart']['category']    
        
        dados = [
            dict(
                valor=x['value'],
                indicador=f"{key}Payout",
                ano=a)
            for key,item in series.items()
            for x,a in zip(item,anos)
        ]

        df_resultado = pd.DataFrame(dados)
        df_resultado['ativo'] = ticker
        df_resultado = df_resultado[['ano','ativo','indicador','valor']]
        
        return df_resultado
