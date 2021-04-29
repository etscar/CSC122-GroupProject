import sys, time
import requests, bs4
import threading, logging
from random import *

# Define constants
WAIT_INTERVAL = 120
LOG_FILE = 'StockPriceLogV1.txt'


def main():
    """
    Clear the log, set up logging, log a start message
    Start up a thread for each stock in stock_list
    Call get_quote(symbol) to get current stock prices
    Sleep a little to allow the stock prices to be logged
    Have the user enter CTRL-C to stop the program.
    """

    open(LOG_FILE, 'w').close()
    logging.basicConfig(filename=LOG_FILE,
                        level=logging.INFO,
                        format=' %(asctime)s %(message)s ')

    # Log the START of the program ...
    logging.info("StockWatcherV1 - start program")

    # PICK 4 of your own favorite STOCK SYMBOLS
    stock_list = ["XXXX", "YYYY", "ZZZZ", "SSSS"]

    for i in range(len(stock_list)):
        stock = stock_list[i].upper()
        print("Begin watch for " + stock)

        # Start a stock watch thread …
        #    target = function to be executed by thread
        #    args = arguments to be passed to target
        thread = threading.Thread(target=get_quote,
                                  args=(stock,))
        # Make this thread the daemon
        thread.setDaemon(True)

        # Start the thread
        thread.start()

    # Sleep for a few seconds to print msgs
    time.sleep(5)

    # Use a try-except to catch the CTRL-C ...
    try:
        input("\nHit CTRL-C to stop recording.\n\n")
    except:
        pass

        # Log the END of the program ...
    logging.info("StockWatcherV1 - end program")


def get_quote(symbol):
    """
    Get a stock quote for the given stock symbol
    Simulate price comparisons using prices LIST
    Compare current price with previous price
    Log start watching, differences and stop watching
    """

    # DUMMY PRICES to simulate prices from Yahoo Finance
    # Change $$$’s to 6 different integer price values
    # Example: '134', '136', '133' …
    prices = ['$$$', '$$$', '$$$', '$$$', '$$$', '$$$']
    price = prices[0]
    # Change prev_price $$$ to an integer price value
    # The value should be close to prices above (eg. '135')
    prev_price = '$$$'

    text = "Start watching " + symbol + ": Price: " + price
    print(text)
    logging.info(text)

    i = 0

    # Start watching and continue until CTRL-C
    while True:

        # Get a price from prices LIST
        price = prices[i % 6]

        # Send price for symbol to log
        logging.info(symbol + "\t" + price)

        i = i + 1

        # Check for price difference and send email,
        # if different
        if price != prev_price:
            text = symbol + " now at " + price + \
                   "; was at " + prev_price
            print(text)
            send_email(text)

            # update prev_price to create difference
            prev_price = price
        # Allow time for messages
        time.sleep(WAIT_INTERVAL)


def send_email(msg):
    """
    Simulate sending an email with simple print()
    """
    print("SEND-EMAIL: " + msg)


main()
