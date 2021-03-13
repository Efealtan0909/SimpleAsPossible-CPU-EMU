USELAST = input('Use Last Program (Y/N) [DEFAULT: N]> ')

if USELAST.lower() == 'y':
    with open('lastprogram', 'r') as f:
        FILE = f.read().replace('\n', '')
else:
    FILE = input('Enter Program Name> ')

DATA = []

if FILE.find('.SAPP') != -1:
    with open('lastprogram', 'w') as f:
        f.write(FILE)
    with open(FILE, 'r') as f:
        DATA = f.read().split('\n')
else:
    with open('lastprogram', 'w') as f:
        f.write(FILE+'.SAPP')
    with open(FILE+'.SAPP', 'r') as f:
        DATA = f.read().split('\n')

def Read(A):
    try:
        if (len(DATA)-1) == int(A):
            raise IndexError()
        return DATA[int(A)]
    except IndexError:
        return 'END'
