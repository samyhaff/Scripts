#!/usr/bin/python3 

import os 
import sys

stream = os.popen("sound")
volume = int(stream.read())

arg = sys.argv
operation = arg[1]
value = int(arg[2])

if operation == "inc" and volume <= 150 - value:
    os.system('pactl set-sink-volume  @DEFAULT_SINK@ +' + str(value) + '%')
elif operation == "dec":
    os.system('pactl set-sink-volume  @DEFAULT_SINK@ -' + str(value) + '%')
