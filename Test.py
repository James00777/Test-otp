
import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from libzam import main_d
    main_d()
elif bit == '32bit':
    from libzam import main_d
    main_d()
