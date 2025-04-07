import os
import configparser
    
class PropertyUtil:
    @staticmethod
    def getPropertyString():
        path = os.path.join(os.path.dirname(__file__), 'db_config.properties')
        config = configparser.ConfigParser()
        config.read(path)

        db_config = config['database']
        connectionString = (
            f"Driver={db_config['DRIVER_NAME']};"
            f"Server={db_config['SERVER']};"
            f"Database={db_config['DATABASE']};"
            f"UID={db_config['USERNAME']};"
            f"PWD={db_config['PASSWORD']};"
        )

        return connectionString