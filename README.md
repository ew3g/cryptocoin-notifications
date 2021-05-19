# cryptocoin-notifications
script for monitoring of cryptocoin prices and alert drops on a notify.run channel

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs
```bash
pip install -r requirements.txt
```

Edit the file [secret.py](https://github.com/lukeSkywallk/cryptocoin-notifications/blob/master/secret.py) and set the SECRET_COIN_MARKET_CAP with your [key](SECRET_COIN_MARKET_CAP) and set NOTIFY_RUN_URL with your channel [url](https://notify.run/)

Edit the file [constants.py](https://github.com/lukeSkywallk/cryptocoin-notifications/blob/master/constants.py) and set the COINS to watch, the JOB_RUNNING_MINUTES_INTERVAL in minutes, the DEFAULT_TIMEZONE and FORMAT_DATETIME

## Usage

```bash
python run.py
```

After running the script, go your notify.run channel and subscribe to receive the updates

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/)

## Thanking
Source code for the [schedule](https://pypi.org/project/schedule/) lib. Credits to [Dan Bader](https://github.com/dbader).
Source code for the [pytz](https://pypi.org/project/pytz/) lib. Credits to [Dan Bader](mailto:stuart@stuartbishop.net).