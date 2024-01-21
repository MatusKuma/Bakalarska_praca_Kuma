import holding
import rsi_sma_strategy
import rsi_strategy
import sma_strategy
import wait_till_target_reached_close_open as target


#target.start_trading(10000, 5, "bull_market_target.csv", "bull_target_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2020-10-31 09:00:00", "2021-03-05 00:00:00")
#target.start_trading(10000, 5, "bear_market_target.csv", "bear_target_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2021-12-07 19:00:00", "2022-06-19 09:00:00")
#target.start_trading(10000, 5, "sideways_market_target.csv", "sideways_target_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2023-08-17 16:00:00", "2023-09-21 23:00:00")
#target.start_trading(10000, 5, "stats/alltime_target.csv", "stats/alltime_target_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2020-10-31 04:00:00", "2023-09-21 23:00:00")


#holding.start_trading(10000, "bull_market_hold.csv", "bull_market_hold_stat.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2020-10-31 09:00:00", "2021-03-05 00:00:00")
#holding.start_trading(10000, "bear_market_hold.csv", "bear_market_hold_stat.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2021-12-07 19:00:00", "2022-06-19 09:00:00")
#holding.start_trading(10000, "sideways_market_hold.csv", "sideways_hold_stat.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2023-08-17 16:00:00", "2023-09-21 23:00:00")
#holding.start_trading(10000, "stats/alltime_hold.csv", "stats/alltime_hold_stat.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2020-10-31 09:00:00", "2023-11-23 23:00:00")

#rsi_strategy.start_trading(10000, "stats/rsi_indicator_bull.csv", "stats/rsi_indicator_bull_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv",  "2020-10-31 09:00:00", "2021-03-05 00:00:00")
#rsi_strategy.start_trading(10000, "stats/rsi_indicator_alg_bear.csv", "stats/rsi_indicator_bear_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2021-12-07 19:00:00", "2022-06-19 09:00:00")
#rsi_strategy.start_trading(10000, "stats/rsi_indicator_alg_sideways.csv", "stats/rsi_indicator_sideways_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2023-08-17 16:00:00", "2023-09-21 23:00:00")
#rsi_strategy.start_trading(10000, "stats/rsi_indicator_alg_altime.csv", "stats/rsi_indicator_alltime_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2019-10-31 09:00:00", "2023-09-21 23:00:00")

#sma_strategy.start_trading(10000, "stats/sma_indicator_bull.csv", "stats/sma_indicator_bull_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv",  "2020-10-31 09:00:00", "2021-03-05 00:00:00")
#sma_strategy.start_trading(10000, "stats/sma_indicator_alg_bear.csv", "stats/sma_indicator_bear_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2021-12-07 19:00:00", "2022-06-19 09:00:00")
#sma_strategy.start_trading(10000, "stats/sma_indicator_alg_sideways.csv", "stats/sma_indicator_sideways_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2023-08-17 16:00:00", "2023-09-21 23:00:00")
#sma_strategy.start_trading(10000, "stats/sma_indicator_alg_altime.csv", "stats/sma_indicator_alltime_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2019-10-31 09:00:00", "2023-09-21 23:00:00")

rsi_sma_strategy.start_trading(10000, "stats/rsi_sma_indicator_bull.csv", "stats/rsi_sma_indicator_bull_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv",  "2020-10-31 09:00:00", "2021-03-05 00:00:00")
rsi_sma_strategy.start_trading(10000, "stats/rsi_sma_indicator_alg_bear.csv", "stats/rsi_sma_indicator_bear_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2021-12-07 19:00:00", "2022-06-19 09:00:00")
rsi_sma_strategy.start_trading(10000, "stats/rsi_sma_indicator_alg_sideways.csv", "stats/rsi_sma_indicator_sideways_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2023-08-17 16:00:00", "2023-09-21 23:00:00")
rsi_sma_strategy.start_trading(10000, "stats/rsi_sma_indicator_alg_altime.csv", "stats/rsi_sma_indicator_alltime_stats.csv", 0.001, "BTCUSD_1h_with_indicators.csv", "2019-10-31 09:00:00", "2023-09-21 23:00:00")
