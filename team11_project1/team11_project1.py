import getopt, sys

class state:
    memory = []
    PC = 96
    instruction = []
    opcode = []
    validInstr = []
    address = []
    arg1 = []
    arg2 = []
    arg3 = []
    numInstructions = 0
    cycle = 1
    R = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #registers 0-32 (for _sim.txt)
    inputFileName = ''
    outputFileName = ''
    stuff = ''
    
    # def __init__( self, instrs, opcodes, mem, valids, addrs, args1, args2, args3, numInstrs ):
    #     self.instruction = instrs
    #     self.opcode = opcodes
    #     self.memory = mem
    #     self.validInstr = valids
    #     self.address = addrs
    #     self.numInstructions = numInstrs
    #     self.arg1 = arg1
    #     self.arg2 = arg2
    #     self.arg3 = arg3
    def __init__( self, valids, op, arg1, arg2, arg3, instrs):
        self.instruction = instrs
        self.opcode = op
        self.validInstr = valids
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3


        
    # def disassembler( ):
        
    #     if R[0] == 0: 

    #     elif R[0] == 1:
    #         {
    #             #opcode 0
    #             if R[1:6] == 00000:
    #                 {
    #                     #functions
    #                     if R[26:32] == 000000:
    #                         {
    #                             if R[0:32] == 00000000000000000000000000000000:
                                
    #                             elif #SLL
    #                         }
                            
    #                     elif R[26:32] == 000010:
    #                         #SRL
    #                     elif R[26:32] == 001000:
    #                         #JR
    #                     elif R[26:32] == 001010:
    #                         #MOVZ
    #                     elif R[26:32] == 100000:
    #                         #ADD
    #                     elif R[26:32] == 100010:
    #                         #SUB
    #                     elif R[26:32] == 100100:
    #                         #AND
    #                     elif R[26:32] == 100101:
    #                         #OR   
    #                 }
                
    #             #opcode 1
    #             elif R[1:6] == 00001:
    #                 #BLTZ
                    
    #             #opcode 2
    #             elif R[1:6] == 00010:
    #                 #J
                    
    #             #opcode 4
    #             elif R[1:6] == 00100:
    #                 #BEQ
                
    #             #opcode 8
    #             elif R[1:6] == 01000:
    #                 #ADDI
                    
    #             #opcode 0x2b
    #             elif R[1:6] == 01011:
    #                 #SW
                
    #             #opcode 0x23
    #             elif R[1:6] == 00011:
    #                 #LW
                
    #             #opcode 0x1C
    #             elif R[1:6] == 11100:
    #                 #MUL
    #         }
            
            

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

    f = open( inputFileName, 'r')

   # wrong wrong wrong. so tired. dont want to delete anything that might be useful tomorrow
 
   #  stuff = f.readline()
   #  stuff = int(float(f.readline()))

   # # computer = state(stuff.parse[0:1], stuff.parse[1:6], stuff.parse[6:11], 
   #  #     stuff.parse[11:16], stuff.parse[16:21], stuff.parse[21:26], stuff.parse[26:31])

    




    # print '********TESTING**********'
    # print 'inputfile: ', inputFileName
    # print 'outputfile: ', outputFileName

    # outFile = open( outputFileName + "_sim.txt", 'w' )
    # outFile.close()
    # outFile = open( inputFileName + "_dis.txt", 'w' )
    # outFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])

            
