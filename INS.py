import RAM
import CONSOLE
import time
import threading

# INSTABLE
# NOP
# MOV 
# ADD 
# SUB 
# MUL 
# DIV 
# JMP 
# JE 
# JNE
# JGT
# JLT
# BOP
# END / HALT

# REGISTERS
RAD  = "0"      # A           Regsiter (GPR) 
RBD  = "0"      # B           Register (GPR) 
ACC  = "0"      # Accumulator Register (ALU)
BOR  = "0"      # Binary OP   Register (BOP)
LRD  = "0"      # Line        Register (INS) 
INSR = ""       # Instruction Register (INS)  

# VARS
LOOP = False

# FUNCTIONS
def Start(Speed):
    global LOOP
    LOOP = True
    CLKS = Speed
    while LOOP:
        OUTPUT = INFLOOP()
        if not OUTPUT:
            break
        time.sleep(CLKS)

def INFLOOP():
    global LOOP
    # DEFINITONS
    OPERATION = "NONE"
    global RAD
    global RBD
    global ACC
    global BOR
    global LRD
    global INSR
    INSR = CONSOLE.Read(LRD)
    INSS = INSR.split(' ')
    OPCODE = INSS[0]

    # INSTRUCTIONS
    if OPCODE.find('MOV') == 0:
        OPERATION = "MOV"
        if INSS[1][0] == '!':
            if INSS[2].find('RA') == 0:
                RAD = RAM.Read(INSS[1].replace('!', ''))
            elif INSS[2].find('RB') == 0:
                RBD = RAM.Read(INSS[1].replace('!', ''))
            elif INSS[2].find('ACC') == 0:
                ACC = RAM.Read(INSS[1].replace('!', ''))
        else:
            if INSS[1].find('RA') == 0:
                if INSS[2][0] == '!':
                    RAM.Write(INSS[2].replace('!', ''), RAD)
                else:
                    if INSS[2].find('RB') == 0:
                        RBD = RAD
                    elif INSS[2].find('ACC') == 0:
                        ACC = RAD
            elif INSS[1].find('RB') == 0:
                if INSS[2][0] == '!':
                    RAM.Write(INSS[2].replace('!', ''), RBD)
                else:
                    if INSS[2].find('RA') == 0:
                        RAD = RBD
                    elif INSS[2].find('ACC') == 0:
                        ACC = RBD
            elif INSS[1].find('ACC') == 0:
                if INSS[2][0] == '!':
                    RAM.Write(INSS[2].replace('!', ''), ACC)
                else:
                    if INSS[2].find('RA') == 0:
                        RAD = ACC
                    elif INSS[2].find('RB') == 0:
                        RBD = ACC
            elif INSS[1].find('BOR') == 0:
                if INSS[2][0] == '!':
                    RAM.Write(INSS[2].replace('!', ''), BOR)
                else:
                    if INSS[2].find('RA') == 0:
                        RAD = BOR
                    elif INSS[2].find('RB') == 0:
                        RBD = BOR
                    elif INSS[2].find('ACC') == 0:
                        RBD = BOR
            else:
                if INSS[2].find('RA') == 0:
                    RAD = INSS[1]
                elif INSS[2].find('RB') == 0:
                    RBD = INSS[1]
                elif INSS[2].find('ACC') == 0:
                    ACC = INSS[1]
    
    elif OPCODE.find('ADD') == 0:
        OPERATION = "ADD"
        ACC = str(int(ACC) + int(INSS[1]))

    elif OPCODE.find('SUB') == 0:
        OPERATION = "SUB"
        ACC = str(int(ACC) - int(INSS[1]))
    
    elif OPCODE.find('MUL') == 0:
        OPERATION = "MUL"
        ACC = str(int(ACC) * int(INSS[1]))
    
    elif OPCODE.find('DIV') == 0:
        OPERATION = "DIV"
        ACC = str(int(ACC) / int(INSS[1]))

    elif OPCODE.find('JMP') == 0:
        OPERATION = "JMP"
        LRD = INSS[1]
    
    elif OPCODE.find('JE') == 0:
        OPERATION = "JE"
        if INSS[1][0] == '!':
            if INSS[2][0] == '!':
                if RAM.Read(INSS[1].replace('!', '')) == RAM.Read(INSS[2].replace('!', '')):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if RAM.Read(INSS[1].replace('!', '')) == INSS[2]:
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
        else:
            if INSS[2][0] == '!':
                if INSS[1] == RAM.Read(INSS[2].replace('!', '')):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if INSS[1] == INSS[2]:
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
    
    elif OPCODE.find('JNE') == 0:
        OPERATION = "JNE"
        if INSS[1][0] == '!':
            if INSS[2][0] == '!':
                if RAM.Read(INSS[1].replace('!', '')) != RAM.Read(INSS[2].replace('!', '')):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if RAM.Read(INSS[1].replace('!', '')) != INSS[2]:
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
        else:
            if INSS[2][0] == '!':
                if INSS[1] != RAM.Read(INSS[2].replace('!', '')):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if INSS[1] != INSS[2]:
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
    
    elif OPCODE.find('JGT') == 0:
        OPERATION = "JGT"
        if INSS[1][0] == '!':
            if INSS[2][0] == '!':
                if int(RAM.Read(INSS[1].replace('!', ''))) > int(RAM.Read(INSS[2].replace('!', ''))):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if int(RAM.Read(INSS[1].replace('!', ''))) > int(INSS[2]):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
        else:
            if INSS[2][0] == '!':
                if int(INSS[1]) > int(RAM.Read(INSS[2].replace('!', ''))):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if int(INSS[1]) > int(INSS[2]):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
    
    elif OPCODE.find('JLT') == 0:
        OPERATION = "JLT"
        if INSS[1][0] == '!':
            if INSS[2][0] == '!':
                if int(RAM.Read(INSS[1].replace('!', ''))) < int(RAM.Read(INSS[2].replace('!', ''))):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if int(RAM.Read(INSS[1].replace('!', ''))) < int(INSS[2]):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
        else:
            if INSS[2][0] == '!':
                if int(INSS[1]) < int(RAM.Read(INSS[2].replace('!', ''))):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
            else:
                if int(INSS[1]) < int(INSS[2]):
                    LRD = INSS[3]
                else:
                    LRD = str(int(LRD) + 1)
    
    elif OPCODE.find('BOP') == 0:
        OPERATION = "BOP"
        if INSS[1] == 'AND':
            # AND
            if RAD.find('1') == 0 and RBD.find('1') == 0:
                BOR = '1'
            else:
                BOR = '0'
        elif INSS[1] == 'OR':
            # OR
            if RAD.find('1') == 0 or RBD.find('1') == 0:
                BOR = '1'
            else:
                BOR = '0'
        elif INSS[1] == 'NOT':
            # NOT
            if RAD.find('1') == 0:
                BOR = '0'
            else:
                BOR = '1'
        
    
    elif OPCODE.find('END') == 0 or OPCODE.find('HALT') == 0:
        OPERATION = "END"
        LOOP = False
    
    print('__________________')
    print('\nREGISTER INFO\n')
    print('RAD      | '+RAD)
    print('RBD      | '+RBD)
    print('ACC      | '+ACC)
    print('BOR      | '+BOR)
    print('LRD      | '+LRD)
    print('INSR     | '+INSR)
    print('\nOPERATION INFO\n')
    print('OP       | '+INSR)
    print('OPCODE   | '+OPCODE)
    print('INS      | '+OPERATION)
    print('\nRAM INFO\n')
    COUNTERD = "0"
    while int(COUNTERD) <= 15:
        if int(COUNTERD) > 9:
            print(COUNTERD+' : '+RAM.Read(COUNTERD))
        else:
            print(COUNTERD+'  : '+RAM.Read(COUNTERD))
        COUNTERD = str(int(COUNTERD) + 1)

    if not LOOP:
        print('\n')
    else:
        if OPERATION != "JMP" and OPERATION != "JE" and OPERATION != "JNE" and OPERATION != "JGT" and OPERATION != "JLT":
            LRD = str(int(LRD) + 1)

    return LOOP
