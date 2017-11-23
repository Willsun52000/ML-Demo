# HUA HAO

import os
import sys
import time
import datetime

def Time_Dlay(t):
    time.sleep(t)


def Status_Print(status, n):
    t_now = time.localtime()
    t = str(t_now.tm_year) + '-' + str(t_now.tm_mon) + '-' + str(t_now.tm_mday) + '  ' + str(t_now.tm_hour) + ':' + str(t_now.tm_min) + ':' + str(t_now.tm_sec)
    if n==1:
        print('*** ', status,'Start At:', t)
    elif n==0:
        print('*** ', status,'End At:', t)
    else:
        print('Wrong Status Setting')