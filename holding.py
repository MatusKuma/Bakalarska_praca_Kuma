from trade_lib.data_manager import save_trades_to_file, save_stat_to_file, load_data
from trade_lib.my_trade_library import count_trading_fee, open_trade, close_trade, \
    print_trade_info, print_total_statistics, calculate_stats, create_plot
from Account import Account

# Start trading
def exec_trading(df, my_account, trade_file, stat_file, trading_fee_rate, date_from, date_to):
    try:
        open_index = df.columns.get_loc("open")
        close_index = df.columns.get_loc("close")
        date_index = df.columns.get_loc("date")
    except KeyError:
        print("Column not found!")
        return

    trades = []
    trade_number = 1
    is_open = False
    close_price = None
    date = None
    prices = []
    balance = []
    last_price = 0
    balance_value = my_account.quote_balance
    balance.append(balance_value)

    for _, row in df.iterrows():
        open_price = row.iloc[open_index]
        date = row.iloc[date_index]
        prices.append(open_price)
        if last_price != 0:
            balance_value *= (open_price / last_price)
            balance.append(balance_value)
        last_price = open_price
        if not is_open:
            trade_info = open_trade(trade_number, open_price, my_account, trading_fee_rate, 1, date)
            trades.append(trade_info)
            print_trade_info(trade_info)
            is_open = True
        close_price = row.iloc[close_index]


    trade_info = close_trade(trades, trade_number, close_price, my_account, trading_fee_rate, date)
    trades.append(trade_info)
    print_trade_info(trade_info)

    save_trades_to_file(trades, trade_file)
    stats = calculate_stats(trades, date_from, date_to)
    save_stat_to_file([stats], stat_file)
    print_total_statistics(trades, date_from, date_to)
    create_plot(stat_file, balance, prices)


def start_trading(initial_balance, trade_file, stat_file, trading_fee, data_file, date_from, date_to):

    # Trading parameters
    money = initial_balance
    trade_file = trade_file
    trading_fee_rate = trading_fee
    file = load_data(data_file)
    index_start = file[file['date'] == date_from].index.tolist()[0]
    index_end = file[file['date'] == date_to].index.tolist()[0]
    file = file[index_start:index_end]
    stat_file = stat_file
    my_account = Account(quote_balance=money, base_balance=0, quote_debt=0, base_debt=0, available=money)
    exec_trading(file, my_account, trade_file, stat_file, trading_fee_rate, date_from, date_to)
