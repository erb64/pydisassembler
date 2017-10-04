import getopt, sys

class state:
    memory = [] #only what is in the file
    memoryd = [] #decimal values in memory
    mem = [] #changing memory
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
        offset = 0
        towrite = ''
        sfile.write('====================\n')
        for i in range(self.numInstructions):

            dfile.write(self.validInstr[i] + ' ' + self.opcode[i] + ' ' 
                + self.arg0[i] + ' ' + self.arg1[i] + ' ' + self.arg2[i] 
                + ' ' + self.arg3[i] + ' ' + self.instruction[i] + '\t' + str(self.address[i]) )

            if self.validInstr[i] == '0':
                dfile.write( '\tInvalid Instruction\n' ) 
            else: # self.validInstr[i] == '1':
                        #opcode 0
                    if (self.validInstr[i] + self.opcode[i] + self.arg0[i] + self.arg1[i] + self.arg2[i] + self.arg3[i] + self.instruction[i]) == '10000000000000000000000000001101':
                        dfile.write( '\tBREAK\n')
                    elif self.opcode[i] == '00000':
                            #functions
                            if self.instruction[i] == '000000':
                                if (self.validInstr[i] + self.opcode[i] + self.arg0[i] + self.arg1[i] + self.arg2[i] + self.arg3[i] + self.instruction[i]).split() == '00000000000000000000000000000000':
                                    dfile.write( '\tNOP\n')
                                else: #SLL
                                    rd = int(self.arg2[i],2)
                                    rt = int(self.arg1[i],2)
                                    sa = int(self.arg3[i],2)
                                    dfile.write( '\tSLL\tR' + str(rd) + ', R' + str(rt) + ', #' + str(sa) +'\n')        
                            
                            elif self.instruction[i] == '000010': #SRL
                                rd = int(self.arg2[i],2)
                                rt = int(self.arg1[i],2)
                                sa = int(self.arg3[i],2)
                                dfile.write( '\tSRL\tR' + str(rt) + ', R' + str(rd) + ', #' + str(sa) + '\n')
                            
                            elif self.instruction[i] == '001000': #JR
                                rs = int(self.arg0[i],2)
                                dfile.write( '\tJR\tR' + str(rs))

                            elif self.instruction[i] == '001010': #MOVZ
                                rs = int(self.arg0[i],2)
                                rt = int(self.arg1[i],2)
                                rd = int(self.arg2[i],2)
                                dfile.write( '\tMOVZ\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')

                            
                            elif self.instruction[i] == '100000': #ADD
                                rs = int(self.arg0[i],2)
                                rt = int(self.arg1[i],2)
                                rd = int(self.arg2[i],2)
                                dfile.write( '\tADD\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n') 
                            
                            elif self.instruction[i] == '100010': #SUB
                                rs = int(self.arg0[i],2)
                                rt = int(self.arg1[i],2)
                                rd = int(self.arg2[i],2)
                                dfile.write( '\tSUB\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')
                            
                            elif self.instruction[i] == '100100': #AND
                                rs = int(self.arg0[i],2)
                                rt = int(self.arg1[i],2)
                                rd = int(self.arg2[i],2)
                                dfile.write( '\tAND\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n') 
                            
                            elif self.instruction[i] == '100101': #OR
                                rs = int(self.arg0[i],2)
                                rt = int(self.arg1[i],2)
                                rd = int(self.arg2[i],2)
                                dfile.write( '\tOR\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')
    
                    #opcode 1
                    elif self.opcode[i] == '00001': #BLTZ Branch on
                        rs = int(self.arg0[i],2)
                        offset = int((self.arg2[i] + self.arg3[i] + self.instruction[i]),2) * 4# shifted left two bits
                        dfile.write( '\tBLTZ\tR' + str(rs) + ', #' + str(offset) + '\n')
      
                    #opcode 2
                    elif self.opcode[i] == '00010': #J
                        offset = int((self.arg0[i] + self.arg1[i] + self.arg2[i] + self.arg3[i] + self.instruction[i]),2) * 4 #shifted left two bits
                        dfile.write( '\tJ\t#' + str(offset) + '\n')
                        
                    #opcode 4
                    elif self.opcode[i] == '00100': #BEQ
                        rs = int(self.arg0[i],2)
                        rt = int(self.arg1[i],2)
                        offset = int((self.arg2[i] + self.arg3[i] + self.instruction[i]),2)
                        dfile.write( '\tBEQ\tR' + str(rs) + ', R' + str(rt) + ', #' + str(offset) + '\n')
                    
                    #opcode 8
                    elif self.opcode[i] == '01000': #ADDI
                    ##put the stuff into the dis file
                        rs = int(self.arg0[i],2)
                        rt = int(self.arg1[i],2)
                        offset = self.arg2[i] + self.arg3[i] + self.instruction[i]
                        if offset[0:1] == '1':
                            offset = ((int(offset,2) ^ 0b1111111111111111) + 1) * -1
                        else:
                            offset = int(offset,2)
                        towrite = '\tADDI\tR' + str(rt) + ', R' + str(rs) + ', #' + str(offset) + '\n'
                        dfile.write( towrite)

                        ##do the action
                        self.R[rs] = self.R[rt] + offset

                        ##put the stuff in the sim file
                        sfile.write( 'cycle:' + str(self.cycle) + towrite )
                        sfile.write( '\nregisters:\n')
                        self.writeRegs(sfile)
                        #write memory
                        sfile.write( '\ndata:' )
                        # self.writeMem(sfile)
                        self.cycle += 1

                    #opcode 0x2b
                    elif self.opcode[i] == '01011': #SW
                        rt = int(self.arg1[i],2)
                        rd = int(self.arg0[i],2) #base
                        offset = int((self.arg2[i] + self.arg3[i] + self.instruction[i]),2)
                        dfile.write( '\tSW\tR' + str(rt) + ', ' + str(offset) + '(R' + str(rd) + ')\n')
                    
                    #opcode 0x23
                    elif self.opcode[i] == '00011': #LW
                        rt = int(self.arg1[i],2)
                        rd = int(self.arg0[i],2) #base
                        offset = int((self.arg2[i] + self.arg3[i] + self.instruction[i]),2)
                        dfile.write( '\tLW\tR' + str(rt) + ', ' + str(offset) + '(R' + str(rd) + ')\n')
                    
                    #opcode 0x1C
                    elif self.opcode[i] == '11100': #MUL
                        rs = int(self.arg0[i],2)
                        rt = int(self.arg1[i],2)
                        rd = int(self.arg2[i],2)
                        dfile.write( '\tMUL\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')

            self.PC += 4
        for i in range(self.numInstructions - 1, len(self.memory)):
            dfile.write( self.memory[i] + '\t' + str( 96 + 4 * (i + 1)) + '\t' + str(self.memoryd[i]) + '\n')

    def writeRegs( self, sfile ):
        sfile.write('r00:\t')
        for i in range(8):
            sfile.write(str(self.R[i]) + '\t')
        sfile.write('\nr08:\t')
        for i in range(8,16):
            sfile.write(str(self.R[i]) + '\t')
        sfile.write('\nr16:\t')
        for i in range(16,24):
            sfile.write(str(self.R[i]) + '\t')
        sfile.write('\nr24:\t')
        for i in range(24,32):
            sfile.write(str(self.R[i]) + '\t')
        sfile.write('\n')

    def writeMem( self, sfile ):
        sfile.write( str( self.numInstructions*4+96 ) + '\t')



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

    line = f.readline()
    computer = state(line[26:32],line[1:6],line[0:1],line[6:11],
        line[11:16],line[16:21],line[21:26])

    while line[0:32] != '10000000000000000000000000001101': 
        line = f.readline()
        computer.addInstruction(line[26:32],line[1:6],line[0:1],line[6:11],
            line[11:16],line[16:21],line[21:26])
        computer.memory.append(line[0:32])
        computer.memoryd.append(int(line[0:32]))
    
    for line in f:
        computer.memory.append(line[0:32])
        if line[0:1] == '1':
            computer.memoryd.append(((int(line,2) ^ 0b11111111111111111111111111111111) + 1) * -1)
        else: 
            computer.memoryd.append(int(line,2))



    f.close()

    computer.disassembler(disFile,simFile)





    # print '********TESTING**********'
    # print 'inputfile: ', inputFileName
    # print 'outputfile: ', outputFileName

    # outFile = open( outputFileName + "_sim.txt", 'w' )
    # outFile.close()
    
    # disFile.write(line[0:1] + ' ' + line[1:6] + ' ' + line[6:11] + ' ' + line[11:16] + ' ' + 
    #     line[16:21] + ' ' + line[21:26] + ' ' + line[26:31] + '\n')

    simFile.close()
    disFile.close()


if __name__ == "__main__":
    main(sys.argv[1:])

            
