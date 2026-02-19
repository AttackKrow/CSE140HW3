#Take in user input with length checks

inst = input("Enter a 32-bit instruction: ")

while (len(inst) != 32):
    inst = input("Invalid input. Please enter a 32-bit instruction.")

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

match opcode:       #couldnt find an easy pattern for opcodes, idk if you have any ideas for better parsing of type, prints are placeholders
    case 0b0000011:
        print(opcode)
    case 0b0001111:
        print(opcode)
    case 0b0010011:
        print(opcode)
    case 0b0010111:
        print(opcode)
    case 0b0011011:
        print(opcode)
    case 0b0110011:
        print(opcode)

#Print instruction fields in the expected format




