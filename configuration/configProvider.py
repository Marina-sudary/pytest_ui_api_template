import configparser

global_config = configparser.ConfigParser
global_config.read('test_config_ini')

class configProvider:

    def __init__(self) -> None:
        self.config = global_config

    # можно делать общие методы
    def get(self, section:str, prop: str):
        return self.config[section].get(prop)
    
    def getint(self, section:str, prop: str):
        return self.config[section].getint(prop)
    
    #можно делать специфичные методы
    def get_ui_url(self):
        return self.config["ui"].get("base_url")