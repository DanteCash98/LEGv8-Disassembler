import SetUp
import os
import masking_constants as MASKs
import sys


class Disassembler:
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):
        instructions = []
        instructions = SetUp.import_data_file()
#       for i in instruction:
#           print(i)

        output_file_name = SetUp.get_output_filename()

        print("raw output filename is ", output_file_name)

#       print(hex(MASKs.bMASK))
#       print(bin(MASKs.bMask))
#       print(f'{MASKs.bMask:032b}')

        # create an address list with appropriate length
        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        # create an opcode list by selecting the left 11 bits
        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        # decode and dissect

        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            if opcode[i] == 1112:  # ADD
                self.instrSpaced.append(SetUp.bin_to_string_spaced_r(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg3Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1624:  # SUB
                pass
            elif opcode[i] == 1104:  # AND
                pass
            elif opcode[i] == 1160:  # ADDI
                pass
            elif opcode[i] == 1360:  # ORR
                pass
            elif opcode[i] == 1440:  # CBZ
                pass
            elif opcode[i] == 1448:  # CBNZ
                pass
            elif opcode[i] == 1672:  # SUBI
                pass
            elif opcode[i] == 1684:  # MOVZ
                pass
            elif opcode[i] == 1940:  # MOVK
                pass
            elif opcode[i] == 1690:  # LSR
                pass
            elif opcode[i] == 1691:  # LSL
                pass
            elif opcode[i] == 1984:  # STUR
                pass
            elif opcode[i] == 1986:  # LDUR
                pass
            elif opcode[i] == 1692:  # ASR
                pass
            elif opcode[i] == 0:  # NOP
                pass
            elif opcode[i] == 1872:  # EOR
                pass
            elif opcode[i] == 2038 and (int(instructions[i], base=2) & MASKs.specialMask) == 2031591:  #BREAK
                self.instrSpaced.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
            else:  # UNKNOWN
                self.opcodeStr.append("unknown")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                print("i =:  " + str(i))
                print("opcode =:  " + str(opcode[i]))
                sys.exit("You have found an unknown instruction, investigate NOW")


