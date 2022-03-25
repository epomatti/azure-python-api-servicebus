from configparser import ConfigParser


def get_config(config):
    parser = ConfigParser()
    parser.read('config.ini')
    return parser.get('AZURE', config)
