import config
import requester


class Util:
    default_header = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY':
            config.config_file['secrets']['secret_coin_market_cap'],
    }

    default_parameters = {}


util = Util()


def get_data_coins_list():
    return requester.get_request(
        config.config_file['urls']['mock_url_list_coin_market_api'],
        headers=util.default_header,
        params=util.default_parameters)
