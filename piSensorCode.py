from gpiozero import MCP3008
from time import sleep
import RPi.GPIO as IO
"""
<50–250 ppm: Low
300–500 ppm: Ideal
600–900 ppm: Not great
1000–2000 ppm: Bad
>2000: Unacceptable

"""

#ana_val = MCP3008(0)
#voltage = (ana_val.value)*5/1024.0
#TDS_Value = (133.42/voltage*voltage*voltage-255.86*voltage*voltage+857.39*voltage)*0.5
#IO.setmode(IO.BCM)
#IO.setup(9,IO.IN)
#TDS_value = IO.input(9)

while 1:
    
    ana_val = MCP3008(0)
   # voltage = (ana_val.value)*5/1024.0
    TDS_Value = (133.42/ana_val.value*ana_val.value*ana_val.value-255.86*ana_val.value*ana_val.value+857.39*ana_val.value)*0.5
    print("TDS_val: ", (TDS_Value))
    sleep(1)