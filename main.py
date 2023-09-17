from modules.data_processing import read_csv_from_file, form_candlesticks, calculate_ema
from modules.visualization import plot_candlestick_with_ema
from settings import EMA_LENGTH, CSV_ADDRESS


# read price.csv file with the data
data = read_csv_from_file(CSV_ADDRESS)
print(data.head())


# candlesticks creation based on date interval
candlesticks_5min = form_candlesticks(data, '5T')
print(candlesticks_5min.head())

candlesticks_1hour = form_candlesticks(data, '1H')
print(candlesticks_1hour.head())


# EMA calculation
ema_5min = calculate_ema(candlesticks_5min, EMA_LENGTH)
print(ema_5min.head())

ema_1hour = calculate_ema(candlesticks_1hour, EMA_LENGTH)
print(ema_1hour.head())


# call a vizualization function
plot_candlestick_with_ema(candlesticks_5min, ema_5min)
plot_candlestick_with_ema(candlesticks_1hour, ema_1hour)