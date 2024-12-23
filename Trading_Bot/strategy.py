# strategy.py

def execute_strategy(trading_logic):
    """
    Ejecuta una estrategia de trading basada en la lógica y datos históricos.
    
    Args:
        trading_logic (TradingLogic): Objeto que contiene la lógica de trading.
    """
    decision = trading_logic.make_decision()
    
    if decision == "buy":
        print("Decisión: Comprar activo.")
        # Aquí se podría implementar la lógica para realizar una compra real.
        
    elif decision == "sell":
        print("Decisión: Vender activo.")
        # Aquí se podría implementar la lógica para realizar una venta real.
        
    else:
        print("Decisión: Mantener posición.")
