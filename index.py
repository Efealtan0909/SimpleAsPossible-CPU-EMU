import INS

def toBool(Str):
    if Str.find('1') != -1 or Str.find('True') != -1:
        return True
    else:
        return False

INS.Start(float(input('Speed> ')), toBool(input('Debug> ')))
