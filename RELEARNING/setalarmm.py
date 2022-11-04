#a project given by ShijiX
#i think it's a while loop practice

def setAlarm(employed, vacation):
    if employed is True and vacation is True:
        print(False)
    elif employed is False and vacation is True:
        print(False)
    elif employed is False and vacation is False:
        print(False)
    elif employed is True and vacation is False:
        print(True)
    else:
        print(False)
        
setAlarm(employed=True,vacation=False)