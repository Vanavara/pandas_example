# third party
import mplfinance as mpf


def plot_candlestick_with_ema(data, ema):
    """
    Visualization of candlestick graph with EMA
    """
    # dict with the data for vizualization
    apdict = [
        mpf.make_addplot(ema, color='red', label='EMA')
    ]

    # vizualization
    mpf.plot(data, type='candle', style='charles', title='Candlestick with EMA',
             ylabel='Price', addplot=apdict, volume=False, figratio=(10, 6))
