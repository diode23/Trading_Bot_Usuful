# main.py
from data_acquisition import acquire_data
from strategy import execute_strategy
from historical_data import HistoricalData
from trading_logic import TradingLogic

def main():
    # Inicializamos la clase para manejar datos históricos
    historical_data = HistoricalData()
    
    # Adquirimos los datos actuales del mercado
    market_data = acquire_data()
    
    # Guardamos los datos adquiridos en el historial
    historical_data.store(market_data)
    
    # Inicializamos la lógica de trading
    trading_logic = TradingLogic(historical_data)
    
    # Ejecutamos la estrategia de trading basada en los datos históricos
    execute_strategy(trading_logic)

if __name__ == "__main__":
    main()
