def is_valid_ticker(ticker):
    if ticker.info['regularMarketPrice'] is None:
        return False
    return True


def move_ratio(value1, value2):
    return round(((value2 - value1) / value1) * 100, 2)
