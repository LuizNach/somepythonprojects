import time
for x in range (0,5):  
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)
    
    
"""
import sys
import time
for i in range(10):
    print("Loading" + "." * i)
    sys.stdout.write("\033[F") # Cursor up one line
    time.sleep(1)
"""