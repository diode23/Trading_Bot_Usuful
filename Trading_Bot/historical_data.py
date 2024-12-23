# historical_data.py

class HistoricalData:
    def __init__(self):
        self.data = []

    def store(self, market_data):
        """
        Almacena los datos adquiridos en la lista histórica.
        
        Args:
            market_data (dict): Datos del mercado a almacenar.
        """
        self.data.append(market_data)
