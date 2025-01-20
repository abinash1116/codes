import win32com.client
import time
from datetime import datetime, timedelta

speaker=win32com.client.Dispatch("SAPI.SpVoice")
current_time=datetime.now() #current time 
reminder=current_time+timedelta(minutes=1)#assigning time intervals(timedelta)
while True:
    current_time=datetime.now() #check the current time
    if current_time>=reminder:
        speaker.speak("It's a time to drink water stay hydrated")
        reminder=current_time+timedelta(minutes=1) #scheduling the next reminder

    time.sleep(30)