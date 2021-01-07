
import time
import datetime

Ist=[]
for i in range(6):
    Ist.append(datetime.datetime.now())
    time.sleep(2)
for i in Ist:
    print(i)
