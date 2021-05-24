import requester
import config


class Util:
    def get_coin_symbol(self, coin_pair_symbol):
        return coin_pair_symbol[0:3]

    def get_fiat_symbol(self, coin_pair_symbol):
        return coin_pair_symbol[3:6]


class CoinInfo:
    symbol = None
    coin_pair_symbol = None
    converted_fiat_symbol = None
    variation = None
    time_period_variation = None
    bid_fiat_price = None


util = Util()


def get_coin_info_last_day(coin_pair_symbol):
    url = config.config_file['urls']['url_ticker_coin_last_day_binance_api']
    url = url.replace('{COIN_PAIR_SYMBOL}', coin_pair_symbol)

    result = requester.get_request(url)

    coin_info = CoinInfo()
    coin_info.symbol = util.get_coin_symbol(result.get('symbol'))
    coin_info.converted_fiat_symbol = util.get_fiat_symbol(
        result.get('symbol'))
    coin_info.coin_pair_symbol = result.get('symbol')
    coin_info.variation = float(result.get('priceChangePercent'))
    coin_info.bid_fiat_price = float(result.get('bidPrice'))
    coin_info.time_period_variation = 'DAY'

    return coin_info


def get_coin_info_last_hour(coin_pair_symbol):
    url = config.config_file['urls']['url_candles_coin_time_interval']
    url = (url.replace('{COIN_PAIR_SYMBOL}', coin_pair_symbol)
           .replace('{TIME_INTERVAL}', '1m')
           .replace('{TIME_LIMIT}', '60'))

    candles = requester.get_request(url)

    last_candle = candles[len(candles) - 1]
    last_value = float(last_candle[4])

    first_candle = candles[0]
    first_value = float(first_candle[1])

    variation_on_period = ((last_value - first_value) * 100 / first_value)

    coin_info = CoinInfo()
    coin_info.symbol = util.get_coin_symbol(coin_pair_symbol)
    coin_info.converted_fiat_symbol = util.get_fiat_symbol(coin_pair_symbol)
    coin_info.coin_pair_symbol = coin_pair_symbol
    coin_info.variation = float(variation_on_period)
    coin_info.time_period_variation = 'HOUR'

    return coin_info
