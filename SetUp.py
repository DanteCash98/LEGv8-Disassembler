import sys
import masking_constants as MASKs


class SetUp:
    '''Contains supporting functions that are mostly class-based'''

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        '''gets input file name from the cmd line and returns name'''
        input_file_name = None
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-1' and i < (len(sys.argv) -1):
                input_file_name = sys.argv[i + 1]

        return input_file_name

    @classmethod
    def get_output_filename(cls):
        '''gets output file name from cmd line and returns the name'''
        output_file_name = None
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                output_file_name = sys.argv[i + 1]

        return output_file_name

    @classmethod
    def import_data_file(cls):
        '''gets file name from te cmd line and then downloads the input file and returns the list'''
        input_file_name = None
        instructions = None
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) -1):
                input_file_name = sys.argv[i + 1]
        try:
            instructions = [line.rstrip() for line in open(input_file_name, 'r')]
        except IOError:
            print("Could not open input file, check path")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):
        '''Converts binary of various lengths to a standard 32-bit length and return the converted number'''
        if (MASKs.negBitMask & num) > 0:
            num = num | MASKs.extendMask
            num = num ^ 0xFFFFFFFF
            num += 1
            num *= -1
        return num

    @classmethod
    def imm_signed_to_twos_converter(cls, bits):
        msb = bits >> 15  # most significant bit, indicates if negative or positive
        if msb == 0:
            return bits
        return -2 ** 16 + ((bits << 1) >> 1)

    @classmethod
    def bin_to_string_spaced(cls,s):
        spaced_str = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_d(cls, s):
        spaced_str = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_im(cls, s):
        spaced_str = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_cb(cls, s):
        spaced_str = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_i(cls, s):
        spaced_str = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_r(cls, s):
        spaced_str = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spaced_str

    @classmethod
    def bin_to_string_spaced_b(cls, s):
        spaced_str = s[0:6] + " " + s[6:32]
        return spaced_str

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        '''Converts 32 bit signed, handles negative numbers'''
        return num

    @classmethod
    def decimal_to_binary(cls, num):
        '''converts decimal number to binary and prints the number'''
        if num > 1:
            cls.decimal_to_binary(num //2)
        print(num % 2, end='')

    @classmethod
    def binary_to_decimal(cls, binary):
        print("\n")
        print(int(binary, 2))
