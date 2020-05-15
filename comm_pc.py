###############################################################################
# File Name  : comm_pc.py
# Author     : John B.
# Date       : 05/15/2020
# Description: Connect from RPi to PC via Visa Library.
###############################################################################

import visa
import time

print("Searching for Resources...")
rm = visa.ResourceManager('@py')
print(rm)
print(rm.list_resources())

"""
resource = rm.open_resource('ASRL/dev/ttyGS0::INSTR')
resource.read_termination = '\n'
resource.write_termination = '\n'
resource.timeout = 10001 #5s

while True:
    #print(resource.read('\n'))
    print(resource.write('pi_side'))
    time.sleep(1)"""