""" Gets current price and daily % change from SP500, NASDAQ, and Dow Jones"""

from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    """Returns current price and daily % change for 3 major indices in dictionary format"""
    stocks = ["^GSPC", "^IXIC", "^DJI"]
    response = {'^GSPC': None, '^IXIC': None, '^DJI': None}
    for stock in stocks:
        # Create stock object
        stock_object = yf.Ticker(stock)
        # Get data for the past day
        info = stock_object.info
        # Get open price and % change
        open_price = info.get('regularMarketOpen')
        change = round((info.get('regularMarketOpen') - info.get('previousClose')) / info.get('previousClose') * 100, 2)
        # Add to response dictionary
        response[stock] = {'open': open_price, 'change': change}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
