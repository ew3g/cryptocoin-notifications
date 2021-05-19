import coinmarket
import constants
from datetime import datetime
import notifyrun
from pytz import timezone

def job():
  print('Rodando em: %s' %(datetime.now()))

  response_coins = coinmarket.get_data_coins_list()

  for coin in response_coins['data']:
    coin_symbol = coin['symbol']
    if (coin_symbol in constants.COINS or 'ALL' in constants.COINS):

      coin_name = coin['name']
      coin_price = coin['quote']['USD']['price']

      change_one_hour = coin['quote']['USD']['percent_change_1h']
      change_one_day = coin['quote']['USD']['percent_change_24h']

      if change_one_hour > 0:
        dynamic_text_change_one_hour = constants.TEXT_HIGH
      else:
        dynamic_text_change_one_hour = constants.TEXT_LOW

      if change_one_day > 0:
        dynamic_text_change_one_day = constants.TEXT_HIGH
      else:
        dynamic_text_change_one_day = constants.TEXT_LOW

      if (change_one_day <= constants.THRESHOLD_DROP_ONE_DAY or change_one_hour <= constants.THRESHOLD_DROP_ONE_HOUR):

        default_timezone = timezone(constants.DEFAULT_TIMEZONE)
        now = default_timezone.localize(datetime.now()).strftime(constants.FORMAT_DATETIME)

        message = constants.DEFAULT_NOTIFICATION_MESSAGE %(coin_name, coin_symbol, coin_price,
          dynamic_text_change_one_hour, change_one_hour, dynamic_text_change_one_day, 
          change_one_day, now)
        
        notifyrun.notify(message)
        print(message)