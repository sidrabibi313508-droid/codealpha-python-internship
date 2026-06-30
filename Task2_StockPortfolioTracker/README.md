# Stock Portfolio Tracker

A simple Python command-line tool that calculates total investment value based on manually defined stock prices.

## Features

- Add multiple stocks with quantities
- Calculates total investment automatically
- Hardcoded stock price dictionary (easy to edit/extend)
- Save portfolio summary as `.txt` or `.csv` file
- Input validation for invalid stock names and quantities

## Key Concepts Used

- Dictionaries
- Input/Output handling
- Basic arithmetic
- File handling (txt and csv)
- Loops and conditionals

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the script:

```bash
python stock_portfolio_tracker.py
```

(Use `python3` instead of `python` on Mac/Linux if needed)

## Usage

1. The program will display available stock symbols (AAPL, TSLA, GOOGL, MSFT, AMZN)
2. Enter a stock name and quantity when prompted
3. Type `done` when finished adding stocks
4. View your portfolio summary and total investment
5. Choose to save the result as a `.txt` or `.csv` file

## Example

```
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
Enter stock name and quantity (type 'done' to finish)

Stock name: AAPL
Quantity: 10
Added 10 shares of AAPL ($1800)

Stock name: TSLA
Quantity: 5
Added 5 shares of TSLA ($1250)

Stock name: done

----- Portfolio Summary -----
AAPL: 10 shares x $180 = $1800
TSLA: 5 shares x $250 = $1250
Total Investment: $3050
```

## Editing Stock Prices

To add or update stock prices, edit the `stock_prices` dictionary at the top of the script:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}
```

## License

Free to use for learning and personal projects.
