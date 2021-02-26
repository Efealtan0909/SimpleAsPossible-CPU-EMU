DATA = []
while True:
    IN = input()
    if IN.find('RUN') == 0:
        break
    DATA.append(IN)

def Read(ADDR):
    return DATA[int(ADDR)]