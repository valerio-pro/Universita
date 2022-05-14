import random
import time
 
 
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))
 

# per formato 'giorno/mese/anno' ----> modificare in '%d/%m/%Y'
def randomDate(start, end, prop = random.random()):
    return str_time_prop(start, end, '%Y-%m-%d', prop)  # formato 'anno-mese-giorno'
