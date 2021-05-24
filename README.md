# cryptocoin-notifications
script for monitoring of cryptocoin prices and alert drops on a bot in telegram

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs
```bash
pip install -r requirements.txt
```
Create an API KEY on (CoinMarketCap)[https://coinmarketcap.com/api/]

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

Edit the file[config.yml](https://github.com/lukeSkywallk/cryptocoin-notifications/blob/master/config.yml) and set desired parameters, like job_running_minutes_interval, threshold_alert_drop_one_day, threshold_alert_drop_one_hour, coins and timezone

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