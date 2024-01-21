from Account import MyAccount
from trade_lib.my_trade_library import count_profit, open_trade, close_trade, \
    print_trade_info, print_total_statistics, calculate_stats, create_plot
from trade_lib.data_manager import save_trades_to_file, save_stat_to_file, load_data


# Start trading
def exec_trading(df, my_Account, percent, trade_file, stat_file, trading_fee_rate, date_from, date_to):
    try:
        open_index = df.columns.get_loc("open")
        high_index = df.columns.get_loc("high")
        date_index = df.columns.get_loc("date")
        close_index = df.columns.get_loc("close")
    except KeyError:
        print("Column not found!")
        return

    target_price = None
    trades = []
    trade_number = 1
    prices = []
    balance = []
    last_price = 0
    close_price = 0
    date = 0

    for _, row in df.iterrows():
        open_price = row.iloc[open_index]
        high_price = row.iloc[high_index]
        date = row.iloc[date_index]
        close_price = row.iloc[close_index]
        prices.append(open_price)
        balance.append(my_Account.quote_balance)
        if target_price is None:

            trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 1, date)
            trades.append(trade_info)
            print_trade_info(trade_info)

            target_price = round(count_profit(open_price, percent), 2)
            print("Target price set:", target_price)
            print("")

        while high_price >= target_price:
            print("Target reached:", target_price)
            trade_info = close_trade(trades, trade_number, target_price, my_Account, trading_fee_rate, date)
            trades.append(trade_info)
            print_trade_info(trade_info)
            trade_number += 1
            open_price = target_price
            trade_info = open_trade(trade_number, open_price, my_Account, 100, trading_fee_rate, 1, date)
            trades.append(trade_info)
            print_trade_info(trade_info)

            target_price = round(count_profit(open_price, percent), 2)
            print("New target price set:", target_price)
            print("")

    if len(trades) != 0:

        trade_info = close_trade(trades, trade_number, close_price, my_Account, trading_fee_rate, date)
        trades.append(trade_info)
        balance[-1] = my_Account.quote_balance

    save_trades_to_file(trades, trade_file)
    stats = calculate_stats(trades, date_from, date_to)
    save_stat_to_file([stats], stat_file)
    print_total_statistics(trades, date_from, date_to)
    create_plot(stat_file, balance, prices)


def start_trading(initial_balance, percent, trade_file, stat_file, trading_fee, data_file, date_from, date_to):

    # Trading parameters
    my_Account = MyAccount()
    # Set values for the attributes
    my_Account.quote_balance = initial_balance
    my_Account.base_balance = 0
    my_Account.base_debt = 0
    my_Account.available = initial_balance

    percent = percent
    trade_file = trade_file
    trading_fee_rate = trading_fee
    file = load_data(data_file)
    index_start = file[file['date'] == date_from].index.tolist()[0]
    index_end = file[file['date'] == date_to].index.tolist()[0]
    file = file[index_start:index_end]
    stat_file = stat_file

    exec_trading(file, my_Account, percent, trade_file, stat_file, trading_fee_rate, date_from, date_to)
