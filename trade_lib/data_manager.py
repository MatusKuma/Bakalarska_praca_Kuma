import pandas as pd
import os


def load_data(file_path):
    return pd.read_csv(file_path, engine="c", float_precision="round_trip")


def save_trades_to_file(trades, file_name):
    df_trades = pd.DataFrame(trades)

    if not os.path.isfile(file_name):
        df_trades.to_csv(file_name, index=False)
    else:
        df_trades.to_csv(file_name, mode='w', index=False)



def save_stat_to_file(stats, stat_file):
    df_stats = pd.DataFrame(stats)

    if not os.path.isfile(stat_file):
        df_stats.to_csv(stat_file, index=False)
    else:
        df_stats.to_csv(stat_file, mode="w", index=False)


def getRequiredDataFromTrades(trades):
    trades_with_required_data = []
    for trade in trades:
        trade_info = {
            "unix": trade["unix"],
            "date": trade["date"],
            "action": trade["action"],
            "operation": trade["operation"],
            "operation_price": trade["operation_price"],
            "operation_stop_price": trade["operation_stop_price"],
            "price": trade["price"],
            "open": trade["open"],
            "high": trade["high"],
            "low": trade["low"],
            "close": trade["close"]
        }

        trades_with_required_data.append(trade_info)

    return trades_with_required_data

