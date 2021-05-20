import coinmarket
import constants
from datetime import date, datetime
import dateutils
import telegram_send

def job():
  print('Rodando em: %s' %(dateutils
    .get_now_datetime_formatted(constants.DEFAULT_TIMEZONE, constants.FORMAT_DATETIME)))

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

        

        message = constants.DEFAULT_NOTIFICATION_MESSAGE %(coin_name, coin_symbol, coin_price,
          dynamic_text_change_one_hour, change_one_hour, dynamic_text_change_one_day,
          change_one_day, dateutils.get_now_datetime_formatted(constants.DEFAULT_TIMEZONE, constants.FORMAT_DATETIME))

        telegram_send.send(messages=[message])
        print(message)