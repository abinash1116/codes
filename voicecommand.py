import win32com.client 

speaker = win32com.client.Dispatch("SAPI.SpVoice")  # Calling the Dispatch method of the module which  interact with Microsoft Speech SDK to speak  the given input from the keyboard 

lists=["Abinash","Ram","Shyam","Hari","Sita"]
for l in lists:
    speaker.speak(f"shout out to{l}")

