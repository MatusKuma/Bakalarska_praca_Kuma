import matplotlib.pyplot as plt


def count_profit(price, per):
    return round(price * (1 + (per / 100)), 2)


def count_trading_fee(money, trading_fee_rate):
    return money * trading_fee_rate


def open_trade(trade_number, open_price, my_account, quantity, trading_fee_rate, type_of_trade, date):




    if type_of_trade == 1:
        quote_amount = (quantity / 100.0) * my_account.quote_balance
        trading_fee = count_trading_fee(quote_amount, trading_fee_rate)

        my_account.quote_balance = my_account.quote_balance - trading_fee
        long_or_short = "long"
        action = "buy"
        my_account.base_balance = my_account.base_balance + (quote_amount - trading_fee)/open_price
        amount = (quote_amount - trading_fee)/open_price
    else:
        base_amount = ((quantity / 100.0) * my_account.quote_balance)/open_price
        trading_fee = count_trading_fee(base_amount, trading_fee_rate)

        my_account.quote_balance = my_account.quote_balance + (base_amount-trading_fee)*open_price
        long_or_short = "short"
        action = "sell"
        my_account.base_debt = my_account.base_debt + base_amount

    trade_info = {
        "action": action,
        "trade_number": int(trade_number),
        "price": open_price,
        "type": long_or_short,
        "base_amount": amount,
        "quote_amount": quote_amount,
        "quantity": quantity,
        "trading_fee": trading_fee,
        "date": date,
        "quote_balance": my_account.quote_balance,
        "base_balance": my_account.base_balance,
        "quote_debt": my_account.quote_debt,
        "base_debt": my_account.base_debt,
    }

    return trade_info


def close_trade(trades, trade_number, close_price, my_account, trading_fee_rate, date):



    open_price = trades[(trade_number * 2) - 2]['price']
    type_of_trade = trades[(trade_number * 2) - 2]['type']
    quantity = trades[(trade_number * 2) - 2]['quantity']
    amount = trades[(trade_number * 2) - 2]['amount']
    quote = trades[(trade_number * 2) - 2]['quote_amount']
    quote_amount = trades[(trade_number * 2) - 2]['quote_amount'] + trades[(trade_number * 2) - 2]['quote_debt']

    if type_of_trade == 'long':
        profit_percentage = close_price/open_price
        quote_amount *= profit_percentage
        profit = quote_amount - my_account.quote_debt
        my_account.quote_balance = my_account.quote_balance + profit
        my_account.base_balance = 0
        my_account.quote_debt = 0
        my_account.base_debt = 0
        action = "sell"


    else:
        profit_percentage = close_price / open_price
        quote_amount *= profit_percentage
        profit = quote_amount - my_account.quote_debt
        my_account.quote_balance = my_account.quote_balance + profit
        my_account.base_balance = 0
        my_account.quote_debt = 0
        my_account.base_debt = 0
        action = "buy"

    trading_fee = count_trading_fee(my_account.quote_balance, trading_fee_rate)
    my_account.quote_balance = my_account.quote_balance - trading_fee


    trade_info = {
        "action": action,
        "trade_number": int(trade_number),
        "price": close_price,
        "type": type_of_trade,
        "base_amount": amount,
        "quote_amount": quote,
        "trading_fee": trading_fee,
        "quantity": quantity,
        "date": date,
        "quote_balance": my_account.quote_balance,
        "base_balance": my_account.base_balance,
        "base_debt": my_account.base_debt,
        "quote_debt": my_account.quote_debt,

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
