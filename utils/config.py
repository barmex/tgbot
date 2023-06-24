import configparser
import logging
import os
from pathlib import Path

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class Config:
    token = ''
    __config = configparser.ConfigParser()
    __configfile = Path(f'{Path.home()}/config.ini')

    def __init__(self):
        self.token = self.__get_token_from_environment()
        if self.token is None:
            self.token = self.__get_token_from_config()

    def __get_token_from_config(self) -> str:
        if Path.exists(self.__configfile):
            self.__config.read(self.__configfile)
            return self.__config['tgbot']['token']
        else:
            logging.warn(f'Config file {self.__configfile} does not exist.')
            return None

    def __get_token_from_environment(self) -> str:
        return os.environ.get('TGBOT_TOKEN')
