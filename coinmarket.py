import requester
import secret

class Util:
    def default_header_price_coins():
        return 'oi'
    
    default_header = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': secret.SECRET_COIN_MARKET_CAP,
    }

    default_parameters = {}

    def set_parameters(self, start, limit, convert_currency):
        self.default_parameters = {
            'start': start,
            'limit': limit,
            'convert': convert_currency
        }

        return self.default_parameters

class Constants:
    URL_LIST_COIN_MARKET_API = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    MOCK_URL_LIST_COIN_MARKET_API = 'https://run.mocky.io/v3/8525867f-1b56-4c4f-9199-3614a11f1d4f'    
    HEADER_ACCEPTS_CONTENT = 'application/json'
    DEFAULT_START_CRYPTO_LIST_COIN_MARKET_API = 1
    DEFAULT_LIMIT_CRYPTO_LIST_COIN_MARKET_API = 5000
    DEFAULT_CURRENCY_CONVERT_LIST_COIN_MARKET_API = 'USD'

util = Util()
constants = Constants()

def get_data_coins_list():
    return requester.get_request(
        constants.URL_LIST_COIN_MARKET_API, 
        headers=util.default_header, 
        params=util.default_parameters)