print("- in ws_models/config.py")
import os
from ws_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'local':
        config = ConfigLocal()
        print('- ws_models/config: Local')
    case 'dev':
        config = ConfigDev()
        print('- ws_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- ws_models/config: Production')

