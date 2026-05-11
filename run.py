from os import system,remove
from platform import machine
import time
import os
print('Checking For Update...')
system('git pull')
try:remove('noxotp.cpython-312.so')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/Mr-Beta-Version/libs/raw/refs/heads/main/noxotp.cpython-312.so -o noxotp.cpython-312.so;chmod +x noxotp.cpython-312.so;chmod +x noxotp.cpython-312.so')
else:
    exit("32bit Not Available")

import noxotp
