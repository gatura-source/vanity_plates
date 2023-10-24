from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import sys


class vanity:
    def __init__(self, plate):
        self.plate = plate
        self.reason = ''
        self.valid = 0
        self.got_f_num = 0
        self.f_num_index = 0

    def check_punc(self):
        print('Checking for special char')
        for char in self.plate:
            if char in punctuation:
                self.reason = self.reason + 'Contains a special character'
                self.terminate()
        self.check_len()

    def terminate(self):
        print('Terminating')
        if self.valid:
            print(f"The Plate {self.plate} is valid")
            sys.exit(0)
        else:
            print(f"The plate {self.plate} is not valid\nReason :: {self.reason}")
            sys.exit(0)

    def check_len(self):
        print('Checking length')
        if len(self.plate) > 6 or len(self.plate) < 2:
            self.reason = self.reason + 'Length > 6 or Length < 2'
            self.terminate()
        else:
            self.check_first_2()

    def check_first_2(self):
        print('Checking first 2 chars')
        for char in self.plate[:2]:
            if char not in ascii_uppercase:
                self.reason = self.reason + 'First 2 Chars not alphabet'
                self.terminate()
            else:
                for char in self.plate[2:]:
                    if char in digits and char != '0':
                        self.got_first_num = 1
                        self.f_num_index = self.plate.index(char)
                        #print(self.f_num_index)
                        self.check_chars_after_f_num()
                    elif char in ascii_uppercase and self.got_f_num == 1:
                        self.reason = self.reason + 'Alphabet after first digit character'
                        self.terminate()
                    elif char == '0' and self.got_f_num == 0:
                        self.reason = self.reason + '0 is the first number'
                        self.terminate()
                    else:
                        pass

    def check_chars_after_f_num(self):
        print('Checking for characters after first number')
        for char in self.plate[self.f_num_index:]:
            #print(self.plate[self.f_num_index:])
            if char in ascii_uppercase:
                self.terminate()
        self.valid = 1
        self.terminate()

plate = input('Enter your vanity plate here:: ')
check_plate = vanity(str(plate))
check_plate.check_punc()



            

