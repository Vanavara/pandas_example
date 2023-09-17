<h3>Candlestick Chart with EMA Calculation</h3>
This project provides a solution to create a candlestick chart and calculate the Exponential Moving Average (EMA) based on trade data from a CSV file.

<h2>Features</h2>
Read trades from a CSV file.
Aggregate trades into candlesticks based on a given time interval (e.g., 5 minutes, 1 hour).
Calculation of the Exponential Moving Average (EMA) for a given length (e.g., 14 periods).
Visualization of the candlestick chart with EMA.

<h2>Installation</h2>
1. Clone the repository:
git clone https://github.com/Vanavara/candlestick.git
2. Navigate to the project directory:
cd candlestick
3. Install the required packages using pip:
pip install -r requirements.txt

<h2>Usage</h2>
Usage
1. Place your prices.csv file in the project directory or provide the full path to the file in the settings.py script.
2. Run the main.py script.

<h2>Testing</h2>
To run the tests, execute the following command:
python -m unittest test_functions.py

<h2>Dependencies</h2>
pandas
mplfinance

