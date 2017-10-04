import getopt, sys

class state:
    rawMemory = []
    memory = [] #changing memory
    PC = 96
    instruction = []
    address = []
    arg1 = []
    arg2 = []
    arg3 = []
    numInstructions = 0 #includes BREAK
    cycle = 1
    R = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #registers 0-32 (for _sim.txt)
    # inputFileName = ''
    # outputFileName = ''
    
    def __init__( self, mem ):
        self.rawMemory = mem

    def disassemble( self ):
        i = 0
        while True:
            if self.rawMemory[i][0:1] == '0':
                self.instruction.append('Invalid Instruction')
                self.address.append(self.PC + (i * 4))
                self.arg1.append('')
                self.arg2.append('')
                self.arg3.append('')
                self.numInstructions+=1
                i+=1
            else: # self.validInstr[i] == '1':
                        #opcode 0
                    if (self.rawMemory[i] == '10000000000000000000000000001101'):
                        self.instruction.append('BREAK')
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append('')
                        self.arg2.append('')
                        self.arg3.append('')
                        self.numInstructions+=1
                        i+=1
                        break;
                    elif self.rawMemory[i][1:6] == '00000':
                            #functions
                            if self.rawMemory[i][26:32] == '000000':
                                if self.rawMemory[i] == '00000000000000000000000000000000':
                                    self.instruction.append( 'NOP' )
                                    self.validInstr.append('')
                                    self.address.append(self.PC + (i * 4))
                                    self.arg1.append('')
                                    self.arg2.append('')
                                    self.arg3.append('')
                                    self.numInstructions+=1
                                    i+=1
                                else: #SLL Format: SLL rd, rt, sa
                                    self.instruction.append( 'SLL' )
                                    self.address.append(self.PC + (i * 4))
                                    self.arg1.append(int(self.rawMemory[i][16:21],2))
                                    self.arg2.append(int(self.rawMemory[i][11:16],2))
                                    self.arg3.append(int(self.rawMemory[i][21:26],2))
                                    self.numInstructions+=1
                                    i+=1
                                    #dfile.write( '\tSLL\tR' + str(rd) + ', R' + str(rt) + ', #' + str(sa) +'\n')        
                            
                            elif self.rawMemory[i][26:32] == '000010': #SRL Format: SRL rd, rt, sa
                                    self.instruction.append( 'SRL' )
                                    self.address.append(self.PC + (i * 4))
                                    self.arg1.append(int(self.rawMemory[i][16:21],2))
                                    self.arg2.append(int(self.rawMemory[i][11:16],2))
                                    self.arg3.append(int(self.rawMemory[i][21:26],2))
                                    self.numInstructions+=1
                                    i+=1
                                    #dfile.write( '\tSRL\tR' + str(rt) + ', R' + str(rd) + ', #' + str(sa) + '\n')
                            
                            elif self.rawMemory[i][26:32] == '001000': #JR Format: JR rs
                                    self.instruction.append( 'JR' )
                                    self.validInstr.append('')
                                    self.opcode.append('') 
                                    self.address.append(self.PC + (i * 4))
                                    self.arg1.append(int(self.rawMemory[i][6:11],2))
                                    self.arg2.append('')
                                    self.arg3.append('')
                                    self.numInstructions+=1
                                    i+=1
                                    #dfile.write( '\tJR\tR' + str(rs))

                            elif self.rawMemory[i][26:32] == '001010': #MOVZ Format: MOVZ rd, rs, rt
                                self.instruction.append( 'MOVZ' )
                                self.address.append(self.PC + (i * 4))
                                self.arg1.append(int(self.rawMemory[i][16:21],2))
                                self.arg2.append(int(self.rawMemory[i][6:11],2))
                                self.arg3.append(int(self.rawMemory[i][11:16],2))
                                self.numInstructions+=1
                                i+=1
                                #dfile.write( '\tMOVZ\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')

                            elif self.rawMemory[i][26:32] == '100000': #ADD Format: ADD rd, rs, rt
                                self.instruction.append( 'ADD' )
                                self.address.append(self.PC + (i * 4))
                                self.arg1.append(int(self.rawMemory[i][16:21],2))
                                self.arg2.append(int(self.rawMemory[i][6:11],2))
                                self.arg3.append(int(self.rawMemory[i][11:16],2))
                                self.numInstructions+=1
                                i+=1
                   
                            elif self.rawMemory[i][26:32] == '100010': #SUB Format: SUB rd, rs, rt
                                self.instruction.append( 'SUB' )
                                self.address.append(self.PC + (i * 4))
                                self.arg1.append(int(self.rawMemory[i][16:21],2))
                                self.arg2.append(int(self.rawMemory[i][6:11],2))
                                self.arg3.append(int(self.rawMemory[i][11:16],2))
                                self.numInstructions+=1
                                i+=1
                       
                            elif self.rawMemory[i][26:32] == '100100': #AND Format: AND rd, rs, rt
                                self.instruction.append( 'AND' )
                                self.address.append(self.PC + (i * 4))
                                self.arg1.append(int(self.rawMemory[i][16:21],2))
                                self.arg2.append(int(self.rawMemory[i][6:11],2))
                                self.arg3.append(int(self.rawMemory[i][11:16],2))
                                self.numInstructions+=1
                                i+=1
                         
                            elif self.rawMemory[i][26:32] == '100101': #OR Format: OR rd, rs, rt
                                self.instruction.append( 'AND' )
                                self.address.append(self.PC + (i * 4))
                                self.arg1.append(int(self.rawMemory[i][16:21],2))
                                self.arg2.append(int(self.rawMemory[i][6:11],2))
                                self.arg3.append(int(self.rawMemory[i][11:16],2))
                                self.numInstructions+=1
                                i+=1
                           
                    #opcode 1
                    elif self.rawMemory[i][26:32] == '00001': #BLTZ Format: BLTZ rs, offset
                        self.instruction.append( 'BLTZ' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][6:11],2))
                        self.arg2.append(int(self.rawMemory[i][16:32],2) * 4)
                        self.arg3.append('')
                        self.numInstructions+=1
                        i+=1
                  
                    #opcode 2
                    elif self.rawMemory[i][26:32] == '00010': #J
                        self.instruction.append( 'J' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][6:32],2) * 4)
                        self.arg2.append('')
                        self.arg3.append('')
                        self.numInstructions+=1
                        i+=1 
                        
                    #opcode 4
                    elif self.rawMemory[i][26:32] == '00100': #BEQ Format: BEQ rs, rt, offset
                        self.instruction.append( 'BEQ' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][6:32],2) * 4)
                        self.arg2.append('')
                        self.arg3.append('')
                        self.numInstructions+=1
                        i+=1 

                    #opcode 8
                    elif self.rawMemory[i][26:32] == '01000': #ADDI Format: ADDI rt, rs, immediate
                        self.instruction.append( 'ADDI' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][11:16],2))
                        self.arg2.append(int(self.rawMemory[i][6:11],2))
                        self.arg3.append(int(self.rawMemory[i][16:32],2))
                        if self.arg3[i][0:1] == '1':
                            self.arg3[i] = ((self.arg3[i] ^ 0b1111111111111111) + 1) * -1
                        self.numInstructions+=1
                        i+=1 
                     
                    #opcode 0x2b
                    elif self.rawMemory[i][26:32] == '01011': #SW Format: SW rt, offset(base)
                        self.instruction.append( 'SW' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][11:16],2))
                        self.arg2.append(int(self.rawMemory[i][16:32],2))
                        self.arg3.append(int(self.rawMemory[i][0:16],2))
                        i+=1 
                    #opcode 0x23
                    elif self.rawMemory[i][26:32] == '00011': #LW Format: LW rt, offset(base)
                        self.instruction.append( 'LW' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][11:16],2))
                        self.arg2.append(int(self.rawMemory[i][16:32],2))
                        self.arg3.append(int(self.rawMemory[i][0:16],2))
                        i+=1 
                    #opcode 0x1C
                    elif self.rawMemory[i][26:32] == '11100': #MUL Format: MUL rd, rs, rt
                        self.instruction.append( 'AND' )
                        self.address.append(self.PC + (i * 4))
                        self.arg1.append(int(self.rawMemory[i][16:21],2))
                        self.arg2.append(int(self.rawMemory[i][6:11],2))
                        self.arg3.append(int(self.rawMemory[i][11:16],2))
                        self.numInstructions+=1
                        i+=1
        while True:
            self.address.append(self.address.append(self.PC + (i * 4)))
            self.memory.append(int(self.rawMemory[i]),2)
            if self.memory[i][0:1] == '1':
                self.memory[i] = (((self.memory[i] ^ 0b11111111111111111111111111111111) + 1) * -1)
            i+=1
            if i == len(self.rawMemory):
                break

    def printDis(self, dfile):
        for i in range(self.numInstructions):
            dfile.write( self.rawMemory[i][0:1] + ' ' + self.rawMemory[i][1:6] + ' ' + self.rawMemory[i][6:11] + ' ' + self.rawMemory[i][11:16])
            dfile.write( ' ' + self.rawMemory[i][16:21] + ' ' + self.rawMemory[i][21:26] + ' ' + self.rawMemory[i][26:32] + ' ' + self.address[i])
            
            if self.instruction[i] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR', 'MUL']:
                dfile.write( '\t' + self.instruction[i] + '\t\R '+ str(self.arg1[i]) + ', R' + str(self.arg2[i]) + ', R' + str(self.arg3[i]) + '\n')
            elif self.instruction[i] in ['SLL', 'SRL']:
                dfile.write( '\t' + self.instruction[i] + '\tR' + str(self.arg1[i]) + ', R' + str(self.arg2[i]) + ', #' + str(self.arg3[i]) + '\n')
            elif self.instruction[i] in ['BEQ', 'ADDI']:
                dfile.write( '\t' + self.instruction[i] + '\tR' + str(self.arg1[i]) + ', R' + str(self.arg2[i]) + ', #' + str(self.arg3[i]) + '\n')
            elif self.instruction[i] in ['SW', 'LW']:
                dfile.write( '\t' + self.instruction[i] + '\tR' + str(self.arg1[i]) + ', ' + str(self.arg2[i]) + '(R' + str(self.arg3[i]) + ')\n')
            elif self.instruction[i] == 'BLTZ':
                dfile.write( '\tBLTZ\tR' + str(self.arg1[i]) + ', #' + str(self.arg2[i]) + '\n')
            elif self.instruction[i] == 'J':
                dfile.write( '\tJ\t#' + str(self.arg1[i]) + '\n')
            elif self.instruction[i] == 'JR':
                dfile.write( '\tJR\tR' + str(self.arg1[i]) + '\n')
            elif self.instrucion[i] in ['NOP', 'BREAK', 'Invalid Instruction']:
                dfile.write( '\t' + self.instruction[i]+ '\t')
    
        j = 0
        for i in range(self.numInstructions, len(self.rawMemory)):
            dfile.write( self.rawMemory[i][0:32] + '\t' + self.address[i] + '\t' + self.memory[j])
        j += 1

def main(argv):
    words = []

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputFileName = arg
        elif opt in ("-o", "--ofile"):
            outputFileName = arg

    f = open( inputFileName, 'r')
    disFile = open( outputFileName + "_dis.txt", 'w' )
    simFile = open( outputFileName + "_sim.txt", 'w' )

    for line in f:
        words.append(line[0:32])
    computer = state(words)
    computer.disassemble()
    computer.printDis(dfile)

    f.close()

    simFile.close()
    disFile.close()


if __name__ == "__main__":
    main(sys.argv[1:])


   