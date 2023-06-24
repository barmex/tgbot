import configparser
import logging
from pathlib import Path

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
class Config:
    token = ''
    def __init__(self):
        config = configparser.ConfigParser()
        configfile = Path(f'{Path.home()}/config.ini')
        print(Path.exists(configfile))
        if Path.exists(configfile):
            config.read(configfile)
            self.token = config['tgbot']['token']
        else:
            logging.info(f'Config file {configfile} does not exist.')
            self.__create_config()
            logging.info(f'Config file has been created as {configfile}. Please add your Telegram token to it.')
            exit(10)

    def __create_config(self):
        config = configparser.ConfigParser()
        config['tgbot'] = {}
        config['tgbot']['token'] = ''
        configfile = Path(f'{Path.home()}/config.ini')
        with open(configfile, 'w') as cf:
            print(cf.name)
            config.write(cf)
