# data_acquisition.py
import requests

def acquire_data():
    """
    Adquiere datos de mercado utilizando una API.
    
    Returns:
        dict: Datos del mercado.
    """
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    return response.json()
