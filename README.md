# cryptocoin-notifications
script for monitoring of cryptocoin prices and alert drops on a bot in telegram

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs
```bash
pip install -r requirements.txt
```

Create a bot on Telegram, simply by talking to [BotFather](https://core.telegram.org/bots)
Save the received token

After activate your virtualenv, configure your telegram-send
Example:
```
source venv/Scripts/activate
source venv/bin/activate

telegram-send --configure
```

And follow the instructions
    
    - Paste you bot token from Telegram
    
    - Send the code/password on console to the bot

Edit the file [secret.py](https://github.com/lukeSkywallk/cryptocoin-notifications/blob/master/secret.py) and set the SECRET_COIN_MARKET_CAP with your [key](SECRET_COIN_MARKET_CAP)

Edit the file [constants.py](https://github.com/lukeSkywallk/cryptocoin-notifications/blob/master/constants.py) and set the COINS to watch, the JOB_RUNNING_MINUTES_INTERVAL in minutes, the DEFAULT_TIMEZONE and FORMAT_DATETIME, set TOKEN_BOT_TELEGRAM with the received token by BotFather Telegram

## Usage

```bash
python run.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/)

## Thanking
Source code for the [pytz](https://pypi.org/project/pytz/) lib. Credits to [Stuart Bishop](mailto:stuart@stuartbishop.net).

Source code for the [schedule](https://pypi.org/project/schedule/) lib. Credits to [Dan Bader](https://github.com/dbader).

Source code for the [telegram-send](https://pypi.org/project/telegram-send/) lib. Credits to [Rahiel Kasim](https://github.com/rahiel).