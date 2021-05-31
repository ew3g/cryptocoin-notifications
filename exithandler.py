import telegram_send


def exit_handler():
    telegram_send.send(messages=['The script was killed.'])
