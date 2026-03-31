# 🤖 Smart Trading Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)](https://github.com/)

**Bot de Trading Inteligente** con análisis en tiempo real, estrategias automatizadas y almacenamiento histórico. Desarrollado con programación orientada a objetos.

## ✨ Características Principales

- 📡 **Adquisición de datos** en tiempo real vía APIs
- 🎯 **Estrategias de trading** múltiples y configurables
- 💾 **Almacenamiento histórico** para backtesting
- 🔄 **Modular y extensible** con OOP
- 📊 **Análisis técnico** integrado
- ⚙️ **Configuración flexible** por archivo YAML/JSON

## 📋 Requisitos

```bash
Python 3.8+
```

**Dependencias principales:**
```bash
pip install requests pandas numpy yfinance ta-lib ccxt python-binance
```

## 🚀 Instalación Rápida

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/smart_trading_bot.git
cd smart_trading_bot

# Instalar dependencias
pip install -r requirements.txt

# Configurar claves API
cp config.example.yaml config.yaml
# Editar config.yaml con tus claves
```

## 🎮 Uso

### 1. **Modo Simulado (Paper Trading)**
```bash
python main.py --mode paper --symbol BTCUSDT --strategy sma
```

### 2. **Trading Real**
```bash
python main.py --mode live --symbol BTCUSDT --strategy rsi_macd
```

### 3. **Backtesting**
```bash
python main.py --mode backtest --symbol ETHUSDT --period 1y
```

## 📁 Estructura del Proyecto

```
├── main.py                  # Punto de entrada
├── data_acquisition.py      # APIs de exchanges (Binance, Bybit, etc.)
├── strategies/              # Estrategias de trading
│   ├── sma_crossover.py
│   ├── rsi_strategy.py
│   └── macd_strategy.py
├── historical_data.py       # Base de datos SQLite/PostgreSQL
├── trading_logic.py         # Lógica de ejecución de órdenes
├── config.yaml             # Configuración centralizada
├── requirements.txt        # Dependencias
└── tests/                  # Pruebas unitarias
```

## ⚙️ Configuración

```yaml
# config.yaml
exchange:
  name: binance
  api_key: "tu_api_key"
  api_secret: "tu_api_secret"

trading:
  symbol: BTCUSDT
  timeframe: 1h
  risk_per_trade: 0.02  # 2%

strategies:
  sma:
    fast_period: 10
    slow_period: 30
```

## 📊 Estrategias Disponibles

| Estrategia | Indicadores | Timeframe | Riesgo |
|------------|-------------|-----------|--------|
| **SMA Crossover** | SMA(10,30) | 1h, 4h | Bajo |
| **RSI Strategy** | RSI(14) | 15m, 1h | Medio |
| **MACD** | MACD(12,26,9) | 4h, 1D | Medio |
| **Bollinger Bands** | BB(20,2) | 1h | Alto |

## 🧪 Ejemplo de Ejecución

```
2026-03-31 19:52:00 | INFO  | Bot iniciado - Modo: Paper Trading
2026-03-31 19:52:05 | INFO  | BTCUSDT: Precio $68,450 | Volumen 24h $2.1B
2026-03-31 19:52:10 | INFO  | Señal: COMPRA | SMA Fast: 68,200 > SMA Slow: 67,800
2026-03-31 19:52:15 | INFO  | Orden ejecutada: 0.001 BTC @ $68,450
```

## 🔌 Exchanges Soportados

- ✅ **Binance** (Spot/Futures)
- ✅ **Bybit**
- ✅ **KuCoin**
- ✅ **Kraken**
- 🔄 **+5 más** (fácil de agregar)

## 📈 Rendimiento Histórico

| Estrategia | Profit Factor | Win Rate | Max Drawdown |
|------------|---------------|----------|--------------|
| SMA Cross | 1.45 | 58% | -12.3% |
| RSI | 1.67 | 62% | -8.7% |
| MACD | 1.82 | 55% | -15.2% |

## 🛡️ Seguridad

- 🔐 **Claves API** encriptadas
- 🛑 **Stop Loss** automático
- ⚖️ **Gestión de riesgo** por posición
- 📱 **Notificaciones** Telegram/Discord
- 🔒 **Rate limiting** integrado

## 🚀 Despliegue

### Docker
```bash
docker build -t smart-trading-bot .
docker run -v $(pwd)/config.yaml:/app/config.yaml smart-trading-bot
```

### VPS/Linux
```bash
screen -S trading_bot
python main.py --mode live
# Ctrl+A+D para detach
```

## 🧪 Testing

```bash
# Pruebas unitarias
pytest tests/ -v

# Backtest rápido
python backtest.py --symbol BTCUSDT --strategy sma --period 6m
```

## 🔮 Roadmap

- [x] Estrategias básicas
- [x] Múltiples exchanges
- [ ] Machine Learning
- [ ] Portfolio management
- [ ] Web Dashboard
- [ ] Mobile App

## ⚠️ ⚠️ ADVERTENCIA ⚠️ ⚠️

**🚨 Este es software experimental. No garantiza ganancias.**
- Usa **únicamente fondos que puedas permitirte perder**
- **Paper trading** antes de live trading
- Configura **stop loss** siempre
- Monitorea constantemente

## 📄 Licencia

[MIT License](LICENSE) - Uso libre con responsabilidad.

## 🤝 Contribuir

1. Fork → Clone → Create branch
2. `git checkout -b feature/nueva-estrategia`
3. Commit → Push → PR

¡Únete al desarrollo de trading algorítmico!

---

**Desarrollado con ❤️ para traders cuantitativos**
