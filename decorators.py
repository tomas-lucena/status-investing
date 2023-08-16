import requests
from time import sleep

def retry(func,sleep_connection_error=5,sleep_status_code_erro=1):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)

        except requests.exceptions.ConnectionError:
            print("ConnectionError")
            sleep(sleep_connection_error)
            return wrapper(*args, **kwargs)
        
        if response.status_code != 200:
            print("status_code != 200")
            sleep(sleep_status_code_erro)
            return wrapper(*args, **kwargs)
            
        return response 
    return wrapper

