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
