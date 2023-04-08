#@title **4. Make Alive VPS 12 Hours** 
#@markdown  First: Press CTRL + SHIFT + I and Run Script "Auto-click".

#@markdown  Second: Run Script VPS 12 Hours.

import time
alive = True #@param {type:"boolean"}

temps = 0
sec = 3600
while(temps < 43200):
  if(temps == sec):
    sec += 3600
    x = (temps/60)/60
    print("It's been ",x,"  hour...")
  time.sleep(1)
  temps +=1
