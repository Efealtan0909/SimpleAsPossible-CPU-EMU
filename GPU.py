Screen = [
    False, False, False, False,
    False, False, False, False,
    False, False, False, False,
    False, False, False, False,
]

def toInt(B):
    if B:
        return 1
    else:
        return 0

def Draw():
    print(str(toInt(Screen[0]))+'|'+str(toInt(Screen[1]))+'|'+str(toInt(Screen[2]))+'|'+str(toInt(Screen[3])))
    print(str(toInt(Screen[4]))+'|'+str(toInt(Screen[5]))+'|'+str(toInt(Screen[6]))+'|'+str(toInt(Screen[7])))
    print(str(toInt(Screen[8]))+'|'+str(toInt(Screen[9]))+'|'+str(toInt(Screen[10]))+'|'+str(toInt(Screen[11])))
    print(str(toInt(Screen[12]))+'|'+str(toInt(Screen[13]))+'|'+str(toInt(Screen[14]))+'|'+str(toInt(Screen[15]))+'\n')