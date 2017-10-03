import getopt, sys

class state:
    memory = []
    PC = 96
    instruction = []
    opcode = []
    validInstr = []
    address = []
    arg0 = []
    arg1 = []
    arg2 = []
    arg3 = []
    numInstructions = 0 #includes BREAK
    cycle = 1
    R = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #registers 0-32 (for _sim.txt)
    # inputFileName = ''
    # outputFileName = ''
    
    def __init__( self, instrs, opcodes, valids, args0, args1, args2, args3 ):
        self.instruction.append(instrs)
        self.opcode.append(opcodes)
        self.validInstr.append(valids)
        self.arg0.append(args0)
        self.numInstructions += 1
        self.arg1.append(args1)
        self.arg2.append(args2)
        self.arg3.append(args3)
        self.address.append(self.PC)
        self.PC += 4
     
    def addInstruction( self, instrs, opcodes, valids, args0, args1, args2, args3 ):
        self.instruction.append(instrs)
        self.opcode.append(opcodes)
        self.validInstr.append(valids)
        self.arg0.append(args0)
        self.numInstructions += 1
        self.arg1.append(args1)
        self.arg2.append(args2)
        self.arg3.append(args3)
        self.address.append(self.PC)
        self.PC += 4
        
    def disassembler( self,  dfile, sfile):
        rs = 0
        rt = 0
        rd = 0
        sa = 0
        for i in range(self.numInstructions):

            dfile.write(self.validInstr[i] + ' ' + self.opcode[i] + ' ' 
                + self.arg0[i] + ' ' + self.arg1[i] + ' ' + self.arg2[i] 
                + ' ' + self.arg3[i] + ' ' + self.instruction[i] + ' ' + str(self.address[i]) )

            if self.validInstr[i] == '0':
                dfile.write( ' Invalid Instruction\n' ) 
            else: # self.validInstr[i] == '1':
                        #opcode 0
                    if self.opcode[i] == '00000':
                            #functions
                            if self.instruction[i] == '000000':
                                if (self.validInstr[i] + self.opcode[i] + self.arg0[i] + self.arg1[i] + self.arg2[i] + self.arg3[i] + self.instruction[i]).split() == '00000000000000000000000000000000':
                                    dfile.write( ' NOP\n')
                                else: #SLL
                                    rd = int(self.arg2[i],2)
                                    rt = int(self.arg1[i],2)
                                    sa = int(self.arg3[i],2)
                                    dfile.write( ' SLL\tR' + str(rd) + ', R' + str(rt) + ', #' + str(sa) +'\n')        
                            
                            elif self.instruction[i] == '000010': #SRL
                                rd = int(self.arg2[i],2)
                                rt = int(self.arg1[i],2)
                                sa = int(self.arg3[i],2)
                                dfile.write( ' SRL\tR' + str(rt) + ', R' + str(rd) + ', #' + str(sa) + '\n')
                            
                            elif self.instruction[i] == '001000': #JR
                                rs = int(self.arg0[i])
                                dfile.write( ' JR\tR' + str(rs))

                            elif self.instruction[i] == '001010':
                                #MOVZ
                        #     elif self.instruction[i] == 100000:
                        #         #ADD
                        #     elif self.instruction[i] == 100010:
                        #         #SUB
                        #     elif self.instruction[i] == 100100:
                        #         #AND
                        #     elif self.instruction[i] == 100101:
                        #         #OR   
                        # }
                    
                    #opcode 1
                    # elif self.opcode[i].split() == '00001':
                        #BLTZ Branch on

                        
        #             #opcode 2
        #             elif self.opcode[i] == 00010:
        #                 #J
                        
        #             #opcode 4
        #             elif self.opcode[i] == 00100:
        #                 #BEQ
                    
        #             #opcode 8
        #             elif self.opcode[i] == 01000:
        #                 #ADDI
                        
        #             #opcode 0x2b
        #             elif self.opcode[i] == 01011:
        #                 #SW
                    
        #             #opcode 0x23
        #             elif self.opcode[i] == 00011:
        #                 #LW
                    
        #             #opcode 0x1C
        #             elif self.opcode[i] == 11100:
        #                 #MUL
        
        # file.write('\n')
            dfile.write('\n')
            self.PC += 4
            
            

def main(argv):
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

    f = open( inputFileName, 'rb')
    disFile = open( outputFileName + "_dis.txt", 'w' )
    simFile = open( outputFileName + "_sim.txt", 'w' )

    stuff = f.readline()
    computer = state(stuff[26:32],stuff[1:6],stuff[0:1],stuff[6:11],
        stuff[11:16],stuff[16:21],stuff[21:26])

    while True: 
        stuff = f.readline()
        computer.addInstruction(stuff[26:32],stuff[1:6],stuff[0:1],stuff[6:11],
            stuff[11:16],stuff[16:21],stuff[21:26])
        if stuff.strip() == '10000000000000000000000000001101':
            break;

    for line in f:
        computer.memory.append(line)

    f.close()

    computer.disassembler(disFile,simFile)





    # print '********TESTING**********'
    # print 'inputfile: ', inputFileName
    # print 'outputfile: ', outputFileName

    # outFile = open( outputFileName + "_sim.txt", 'w' )
    # outFile.close()
    
    # disFile.write(stuff[0:1] + ' ' + stuff[1:6] + ' ' + stuff[6:11] + ' ' + stuff[11:16] + ' ' + 
    #     stuff[16:21] + ' ' + stuff[21:26] + ' ' + stuff[26:31] + '\n')

    simFile.close()
    disFile.close()


if __name__ == "__main__":
    main(sys.argv[1:])

            
