import matplotlib.pyplot as plt


def count_profit(price, per):
    return round(price * (1 + (per / 100)), 2)


def count_trading_fee(money, trading_fee_rate):
    return money * trading_fee_rate


def open_trade(unix, trade_number, open_price, my_account, quantity, trading_fee_rate, type_of_trade, date, high_price, low_price, close_price):
    quote_amount = (quantity / 100.0) * my_account.quote_balance
    if type_of_trade == 1:

        trading_fee = count_trading_fee(quote_amount, trading_fee_rate)

        my_account.quote_balance = my_account.quote_balance - trading_fee
        long_or_short = "LONG"
        operation = "BUY"
        my_account.base_balance = my_account.base_balance + (quote_amount - trading_fee)/open_price
        base_amount = (quote_amount - trading_fee)/open_price
        operation_stop_price = open_price * 0.95
    else:
        base_amount = ((quantity / 100.0) * my_account.quote_balance)/open_price
        trading_fee = count_trading_fee(base_amount, trading_fee_rate)
        long_or_short = "SHORT"
        operation = "SELL"
        operation_stop_price = open_price * 1.05
        my_account.base_debt = my_account.base_debt + base_amount

    trade_info = {
        "unix": unix,
        "date": date,
        "trade_number": int(trade_number),
        "action": long_or_short,
        "operation": operation,
        "operation_price": open_price,
        "operation_stop_price": operation_stop_price,
        "price": open_price,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "base_amount": base_amount,
        "quote_amount": quote_amount,
        "quantity": quantity,
        "trading_fee": trading_fee,
        "quote_balance": my_account.quote_balance,
        "base_balance": my_account.base_balance,
        "base_debt": my_account.base_debt,
    }

    return trade_info


def close_trade(unix, trades, trade_number, open_price, my_account, trading_fee_rate, date, high_price, low_price, close_price):



    last_price = trades[(trade_number * 2) - 2]['price']
    action = trades[(trade_number * 2) - 2]['action']
    quantity = trades[(trade_number * 2) - 2]['quantity']
    base_amount = trades[(trade_number * 2) - 2]['base_amount']
    quote_amount = trades[(trade_number * 2) - 2]['quote_amount']
    operation_stop_price = trades[(trade_number * 2) - 2]['operation_stop_price']



    if action == 'LONG':
        profit_percentage = open_price / last_price
        quote_amount_close = profit_percentage*quote_amount
        profit = quote_amount_close - quote_amount
        my_account.quote_balance = my_account.quote_balance + profit
        my_account.base_balance = 0

        my_account.base_debt = 0
        operation = "SELL"
        action="CLOSE"


    else:
        debt = my_account.base_debt * open_price
        my_account.quote_balance = my_account.quote_balance + quote_amount - debt
        my_account.base_balance = 0

        my_account.base_debt = 0
        operation = "BUY"
        action = "COVER"

    trading_fee = count_trading_fee(my_account.quote_balance, trading_fee_rate)
    my_account.quote_balance = my_account.quote_balance - trading_fee


    trade_info = {
        "unix": unix,
        "date": date,
        "trade_number": int(trade_number),
        "action": action,
        "operation": operation,
        "operation_price": open_price,
        "operation_stop_price": operation_stop_price,
        "price": open_price,
        "open": action,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "base_amount": base_amount,
        "quote_amount": quote_amount,
        "trading_fee": trading_fee,
        "quantity": quantity,
        "quote_balance": my_account.quote_balance,
        "base_balance": my_account.base_balance,
        "base_debt": my_account.base_debt,

    }

    return trade_info


def print_trade_info(trade_info):
    for key, value in trade_info.items():
        if key == "price" or key == "quote_balance" or key == "trading_fee":
            print(f"{key}: {value}")
            continue
        if key == "base_amount":
            print(f"{key}: {value}")
            continue
        print(f"{key}: {value}")
    print("")


def calculate_amount(money, price):
    if money <= 0 or price <= 0:
        return 0

    quantity = money / price
    return round(quantity, 4)


def print_total_statistics(trades, date_from, date_to):
    total_trades = len(trades)
    if total_trades == 0:
        print("No trades!!")
        return
    total_trading_fee = round(sum(trade["trading_fee"] for trade in trades), 2)

    print("\nTotal Statistics:")
    print("Date from: " + date_from)
    print("Date to: " + date_to)
    print("Starting balance: ", trades[0]["quote_balance"]+trades[0]["trading_fee"])
    print("Total Trades:", int(total_trades/2))
    print("Actual Money:", round(trades[total_trades-1]["quote_balance"], 2))
    print("Profit:", round(trades[total_trades-1]["quote_balance"]-(trades[0]["quote_balance"]+trades[0]["trading_fee"]), 2), " EUR")
    print("Total Trading Fee:", total_trading_fee)
    print("")


def calculate_stats(trades, date_from, date_to):
    total_trades = len(trades)
    if len(trades) == 0:
        return []
    total_trading_fee = round(sum(trade["trading_fee"] for trade in trades), 2)
    stats = {
        "Date from": date_from,
        "Date to": date_to,
        "Starting balance": trades[0]["quote_balance"] + trades[0]["trading_fee"],
        "Total Trades": int(total_trades / 2),
        "Actual Money": trades[total_trades - 1]["quote_balance"],
        "Profit": round(trades[total_trades - 1]["quote_balance"] - (trades[0]["quote_balance"] + trades[0]["trading_fee"]), 2),
        "Total Trading Fee": total_trading_fee,
    }
    return stats


def create_plot(title, balance, prices):
    time_hours = []
    for i in range(1, len(balance)+1):
        time_hours.append(i)

    fig, ax1 = plt.subplots()

    ax1.plot(time_hours, balance, 'b-')
    ax1.set_xlabel("Time (hours)")
    ax1.set_ylabel("Balance", color="b")

    ax2 = ax1.twinx()
    ax2.plot(time_hours, prices, "r-")
    ax2.set_ylabel("Price")
    min_limit = min(min(balance) - 500, min(prices) - 500)
    max_limit = max(max(balance) + 500, max(prices) + 500)
    ax1.set_ylim(min_limit, max_limit)
    ax2.set_ylim(min_limit, max_limit)

    plt.title(title)
    plt.show()
