import binance
import config
import dateutils
import telegram_send


def job():
    time_now = dateutils.get_now_datetime_formatted(
        config.config_file['parameters']['timezone'],
        config.config_file['parameters']['format_datetime'])

    print('Running: %s' % (time_now))

    coin_pairs = config.config_file['parameters']['coin_pairs']

    for coin_pair in coin_pairs:
        coin_info_last_hour = binance.get_coin_info_last_hour(coin_pair)
        coin_info_last_day = binance.get_coin_info_last_day(coin_pair)

        threshold_alert_drop_one_day = (config
                                        .config_file['constants']
                                        ['threshold_alert_drop_one_day'])

        threshold_alert_drop_one_hour = (config
                                         .config_file['constants']
                                         ['threshold_alert_drop_one_hour'])

        if(coin_info_last_day.variation <= threshold_alert_drop_one_day
           or coin_info_last_hour.variation <= threshold_alert_drop_one_hour):

            message = ("%s: %.2f %s\nLAST HOUR: %.2f%%\n\
LAST DAY: %.2f%%\n%s") % (
                coin_info_last_day.symbol,
                coin_info_last_day.bid_fiat_price,
                coin_info_last_day.converted_fiat_symbol,
                coin_info_last_hour.variation,
                coin_info_last_day.variation,
                time_now)

            telegram_send.send(messages=[message])
            print(message)
