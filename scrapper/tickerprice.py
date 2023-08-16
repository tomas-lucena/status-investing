from decorators import retry
from header import headers
import pandas as pd
import requests

base_url = "https://statusinvest.com.br/acao/"

class Tickerprice:
    def __init__(self):
        self.endpoint = f"{base_url}tickerprice"
    
    @retry
    def request(self,ticker,type=4):           
        self.data = f"ticker={ticker.lower()}&type={type}&currences[]=1"

        resp = requests.post(self.endpoint, headers=headers, data=self.data)

        return resp
    
    def processa(self,resp):
        if resp.status_code != 200:
            print(f"status_code: {resp.status_code}")
            return None
        
        resp_json = resp.json()[0]

        if not resp_json.get('prices', False):
            return None
    
        df_resultado = pd.DataFrame(resp_json.get('prices', False))
        df_resultado['date'] = pd.to_datetime(df_resultado['date'],format="%d/%m/%y %H:%M")

        return df_resultado
    