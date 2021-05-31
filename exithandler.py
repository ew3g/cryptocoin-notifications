import atexit
import signal
import telegram_send


def exit_handler():
    telegram_send.send(messages=['The script was killed.'])


def register_exit_handler():
    atexit.register(exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGINT, exit_handler)