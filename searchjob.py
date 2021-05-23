import coinmarket
import config
import dateutils
import telegram_send


def job():
    time_now = dateutils.get_now_datetime_formatted(
        config.config_file['parameters']['timezone'],
        config.config_file['parameters']['format_datetime'])

    print('Running: %s' % (time_now))

    response_coins = coinmarket.get_data_coins_list()

    for coin in response_coins['data']:

        coin_symbol = coin['symbol']
        config_coins = config.config_file['parameters']['coins']

        if (coin_symbol in config_coins or 'ALL' in config_coins):

            change_one_hour = coin['quote']['USD']['percent_change_1h']
            change_one_day = coin['quote']['USD']['percent_change_24h']

            threshold_alert_drop_one_day = (config
                                            .config_file['constants']
                                            ['threshold_alert_drop_one_day'])

            threshold_alert_drop_one_hour = (config
                                            .config_file['constants']
                                            ['threshold_alert_drop_one_hour'])

            if (change_one_day <= threshold_alert_drop_one_day
                    or change_one_hour <= threshold_alert_drop_one_hour):

                coin_name = coin['name']
                coin_price = coin['quote']['USD']['price']

                message = ("%s(%s): U$: %.2f\nLAST HOUR DROP: %.2f%%\n\
                LAST DAY DROP: %.2f%%\n%s") % (
                    coin_name, coin_symbol, coin_price, change_one_hour,
                    change_one_day, time_now)

                telegram_send.send(messages=[message])
                print(message)
