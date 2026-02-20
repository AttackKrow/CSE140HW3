import re

#Take in user input with length checks

inst = input("Enter a 32-bit instruction: ")

while (not re.match("^[01]{32}$", inst)):
    inst = input("Invalid input. Please enter a 32-bit binary instruction.")

#print("Instruction:", inst)

inst = int(inst, 2)

#Get opcode and use to determine instruction type
opcode   = inst & 0x7F
rd       = (inst >> 7) & 0x1F
funct3   = (inst >> 12) & 0x7
rs1      = (inst >> 15) & 0x1F 
rs2      = (inst >> 20) & 0x1F
funct7   = (inst >> 25) & 0x7F

#print(opcode)

    # Couldnt find an easy pattern for opcodes, idk if you have any ideas for better parsing of type,
    # prints are placeholders for the function
    # Thinking a function for each type, and another match for the funct3 if relevant, IDK, implement what you think is best
    # 
match opcode:       
    case 0b0000011:
        print(opcode)   #I-type
    case 0b0001111:
        print(opcode)   #I-type
    case 0b0010011:
        print(opcode)   #I-type
    case 0b0010111:
        print(opcode)   #U-type
    case 0b0011011:
        print(opcode)   #I-type
    case 0b0100011:
        print(opcode)   #S-type
    case 0b0110011:
        print(opcode)   #R-type
    case 0b0110111:
        print(opcode)   #U-type
    case 0b0111011:
        print(opcode)   #R-type
    case 0b1100011:
        print(opcode)   #SB-type
    case 0b1100111:
        print(opcode)   #I-type
    case 0b1101111:
        print(opcode)   #UJ-type
    case 0b1110011:
        print(opcode)   #I-type
    case _:
        print("Invalid instruction.")
        exit()

#Print instruction fields in the expected format




