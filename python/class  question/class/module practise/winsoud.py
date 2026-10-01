import winsound

'''main 3 h

2. .Beep(freq, duration)
3. PlaySound(sound,flag)
3.MessageBeep()
Constant	                Purpose
MB_OK	 ->             Normal/default sound
MB_ICONASTERISK	->      Information-type sound
MB_ICONEXCLAMATION	    Warning/exclamation sound
MB_ICONHAND             Error-type sound
MB_ICONQUESTION	        Question-type sound
'''











# # winsound.Beep(1000, 500) #Beep(frequency(in Hz), duration(in ms))
# winsound.Beep(500, 300)
# winsound.Beep(1000, 300)
# winsound.Beep(1500, 300)    #making different sounds 

# winsound.PlaySound(sound, flags) syntax of playsound()

'''
          PlaySound()
                /    \
               /      \
          sound        flags
            ↓            ↓
       WHAT to play   HOW to play it
       '''

# Flag	                    Meaning
# SND_FILENAME	    Treat sound as a filename
# SND_ASYNC	        Don't wait for sound to finish
# SND_LOOP	        Repeat the sound
# SND_ALIAS	        Use a Windows system-sound alias
# SND_NOSTOP	    Don't interrupt a currently playing sound
# SND_PURGE	        Stop sounds being played

# winsound.PlaySound(
#     r"C:\batch19\modules learning\winsound\hello.wav",
#     winsound.SND_FILENAME
# )
winsound.PlaySound("huamain.wav", winsound.SND_FILENAME)

# winsound.MessageBeep() // message beep



# winsound.PlaySound("music.wav", winsound.SND_FILENAME)
# print("Hello")   # hello will be printed after sound finishes(synchronous)

#asynchrounous
# import winsound
# import time
# print("Starting sound...")
# winsound.PlaySound("hello.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# print("Program finished.")