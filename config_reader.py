import ConfigParser
from config_params import ConfigParams

class ConfigReader(object):
    
    @staticmethod
    def get_zcash_miner_path():
        return ConfigReader.__get_config().get(ConfigParams.ZCASH_SECTION, ConfigParams.ZCASH_MINER_PATH)
        
    @staticmethod
    def get_zcash_exec():
        return ConfigReader.__get_config().get(ConfigParams.ZCASH_SECTION, ConfigParams.ZCASH_MINER_EXEC)
    
    @staticmethod
    def __get_config():
        c = ConfigParser.ConfigParser()
        c.read('config.cfg')
        return c
        
    
        