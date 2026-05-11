from os import system,remove
from platform import machine
import time
import os
print('Checking For Update...')
system('git pull')
try:remove('noxotp.so')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/Mr-Beta-Version/libs/raw/refs/heads/main/noxotp.so -o noxotp.so;chmod +x noxotp.so;chmod +x noxotp.so')
else:
    exit("32bit Not Available")

import noxotp
