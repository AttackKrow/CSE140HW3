#Take in user input with length checks

#Get opcode and use to determine instruction type
  opcode   = inst & 0x7F
  rd       = (inst >> 7) & 0x1F
  funct3   = (inst >> 12) & 0x7
  rs1      = (inst >> 15) & 0x1F 
  rs2      = (inst >> 20) & 0x1F
  funct7 =   (inst >> 25) & 0x7F

#Grab and fill relevant fields based on instruction type

#Print instruction fields in the expected format


    # Parse the instruciton for it's fields for printing
def parseType(decInst, type):   # maybe replace with non-generic for each type if itll make funct3 parsing easier
    print("temp")




inst = input("Enter a 32-bit instruction: ")

while (len(inst) != 32):
    inst = input("Invalid input. Please enter a 32-bit instruction.")

print("Instruction:", inst)

opcode = inst[25:32]

print("opcode:", opcode)

match opcode:       #couldnt find an easy pattern for opcodes, idk if you have any ideas for better parsing of type
    case "0000011":
        parseType(inst,'I')
    case "0001111":
        parseType(inst,'I')
    case "0010011":
        parseType(inst,'I')
    case "0010111":
        parseType(inst,'U')
    case "0011011":
        parseType(inst,'I')


