print("- in ws_models/config.py")
import os
from ws_config import ConfigDev, ConfigProd, ConfigWorkstation

if os.environ.get('FLASK_CONFIG_TYPE')=='workstation':
    config = ConfigWorkstation()
    print('- ws_models/config: Local')
elif os.environ.get('FLASK_CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('- ws_models/config: Development')
elif os.environ.get('FLASK_CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('- ws_models/config: Production')

