from Account import MyAccount
from trade_lib.my_trade_library import open_trade, close_trade, \
    print_trade_info, print_total_statistics, calculate_stats, create_plot
from trade_lib.data_manager import save_trades_to_file, save_stat_to_file, load_data


# Start trading
def exec_trading(df, my_Account, trade_file, stat_file, trading_fee_rate, date_from, date_to):
    try:
        open_index = df.columns.get_loc("open")
        date_index = df.columns.get_loc("date")
        rsi_index = df.columns.get_loc('RSI')
    except KeyError:
        print("Column not found!")
        return

    trades = []
    trade_number = 1
    prices = []
    balance = []
    trade_is_open = False
    last_price = 0
    overbought = 70
    oversold = 30
    for index, row in df.iterrows():
        open_price = row.iloc[open_index]
        date = row.iloc[date_index]
        rsi = row.iloc[rsi_index]
        prices.append(open_price)


        if rsi >= overbought:
            if trade_is_open:
                if trades[(trade_number * 2) - 2]['type'] == "short":
                    balance.append(my_Account.quote_balance * (open_price/last_price))
                    last_price = open_price
                    continue
                close_trade_info = close_trade(trades, trade_number, open_price, my_Account, trading_fee_rate, date)
                balance.append(my_Account.quote_balance)
                trades.append(close_trade_info)
                print_trade_info(close_trade_info)
                trade_number += 1
                trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 2, date)
                trades.append(trade_info)
                print_trade_info(trade_info)
                last_price = open_price
                continue
            else:
                trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 2, date)
                trades.append(trade_info)
                print_trade_info(trade_info)
                balance.append(my_Account.quote_balance)
                last_price = open_price
                trade_is_open = True
                continue
        if rsi <= oversold:
            if trade_is_open:
                if trades[(trade_number * 2) - 2]['type'] == "long":
                    balance.append(my_Account.quote_balance * (last_price/open_price))
                    last_price = open_price
                    continue
                close_trade_info = close_trade(trades, trade_number, open_price, my_Account, trading_fee_rate, date)
                balance.append(my_Account.quote_balance)
                trades.append(close_trade_info)
                print_trade_info(close_trade_info)
                trade_number += 1
                trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 1, date)
                trades.append(trade_info)
                print_trade_info(trade_info)
                last_price = open_price
                continue
            else:
                trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 1, date)
                trades.append(trade_info)
                print_trade_info(trade_info)
                balance.append(my_Account.quote_balance)
                trade_is_open = True
                last_price = open_price
                continue
        if len(trades) == 0:
            balance.append(my_Account.quote_balance)
            last_price = open_price
            continue
        if trades[(trade_number * 2) - 2]['type'] == "short":
            balance.append(my_Account.quote_balance * (open_price / last_price))
            last_price = open_price
        else:
            balance.append(my_Account.quote_balance * (last_price/open_price))
            last_price = open_price

    save_trades_to_file(trades, trade_file)
    stats = calculate_stats(trades, date_from, date_to)
    save_stat_to_file([stats], stat_file)
    print_total_statistics(trades, date_from, date_to)
    create_plot(stat_file, balance, prices)


def start_trading(initial_balance, trade_file, stat_file, trading_fee, data_file, date_from, date_to):

    # Trading parameters
    my_Account = MyAccount()
    # Set values for the attributes
    my_Account.quote_balance = initial_balance
    my_Account.base_balance = 0
    my_Account.base_debt = 0
    my_Account.available = initial_balance

    trade_file = trade_file
    trading_fee_rate = trading_fee
    file = load_data(data_file)
    index_start = file[file['date'] == date_from].index.tolist()[0]
    index_end = file[file['date'] == date_to].index.tolist()[0]
    file = file[index_start:index_end]
    stat_file = stat_file

    exec_trading(file, my_Account, trade_file, stat_file, trading_fee_rate, date_from, date_to)
