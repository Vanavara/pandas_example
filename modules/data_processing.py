# third party
import pandas as pd


def read_csv_from_file(prices):
    """
    Data reading from a .csv file
    """
    df = pd.read_csv(prices)
    return df


def form_candlesticks(df, interval='5T'):
    """
    Candlesticks creation based on date interval
    """
    df_copy = df.copy()
    df_copy['TS'] = pd.to_datetime(df['TS'])
    df_copy.set_index('TS', inplace=True)

    ohlc = df_copy['PRICE'].resample(interval).ohlc()
    return ohlc


def calculate_ema(df, periods=14):
    """
    EMA calculation
    """
    ema = df['close'].ewm(span=periods, adjust=False).mean()
    return ema
