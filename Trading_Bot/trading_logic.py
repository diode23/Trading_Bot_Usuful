# trading_logic.py

class TradingLogic:
    def __init__(self, historical_data):
        """
        Inicializa la lógica de trading con datos históricos.
        
        Args:
            historical_data (HistoricalData): Objeto que contiene datos históricos.
        """
        self.historical_data = historical_data

    def make_decision(self):
        """
        Toma una decisión de compra o venta basada en los datos históricos y estrategias simples.
        
        Returns:
            str: "buy", "sell" o "hold" dependiendo de la lógica implementada.
        """
        # Lógica simple: si el último dato es mayor que el penúltimo, comprar; si no, vender.
        if len(self.historical_data.data) < 2:
            return "hold"  # No hay suficiente información para decidir.

        last_price = self.historical_data.data[-1]['rates']['EUR']  # Ejemplo con Euro.
        previous_price = self.historical_data.data[-2]['rates']['EUR']

        if last_price > previous_price:
            return "buy"
        elif last_price < previous_price:
            return "sell"
        
        return "hold"
