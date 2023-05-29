import yfinance as yf

from src.main.util.ticker import move_ratio


def get_ticker_info(ticker_id):
    ticker = yf.Ticker(ticker_id)
    info = ticker.info
    history = ticker.history(period='2d')
    info['closePrice'] = history['Close'].iloc[-1]
    if info['regularMarketPrice'] is None:
        reference_price = history['Close'].iloc[-2]
        info['moveRatio'] = move_ratio(reference_price, info['closePrice'])
    else:
        reference_price = history['Close'].iloc[-1]
        info['moveRatio'] = move_ratio(reference_price, info['regularMarketPrice'])
    return info


def get_ticker_history(ticker_id, period, interval):
    ticker = yf.Ticker(ticker_id)
    return ticker.history(period=period, interval=interval)
