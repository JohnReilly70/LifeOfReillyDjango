import string
import random

class password_gen:


    def check(self):
        if (self.max_upper + self.special) > self.pass_len:
            self.password = "ERROR: password length less than requirements of uppercase and special characters"
        else:
            self.func_password_gen()

    def func_password_gen(self):
        '''
        Uses random.choices with string module which creates a new list from the list in the string module.

        First random.choices deals with the requirement of uppercase chase.
        Second random.choices deals with requirement of special chars.
        Third random.choices deals with any remaining characters required. Have to concatenate string modules are there
            are none without whitespace chars.

        Finishes by running function which converts the list to a string after it being randomly shuffled
        '''
        self.char_array.extend(random.choices(string.ascii_uppercase,k=self.max_upper))
        self.char_array.extend(random.choices(string.punctuation, k=self.special))
        self.char_array.extend(random.choices(string.ascii_letters+string.digits+string.punctuation, k=self.pass_len-self.max_upper-self.special))
        self.conv_list_to_string()

    def conv_list_to_string(self):
        """
        Uses random.shuffle to make sure initial characters aren't the upper and punctuation which were
            initialised first.
        Joins list together to create a string

        """

        random.shuffle(self.char_array)
        self.password = "".join(self.char_array)

    def __init__(self,pass_len,max_upper,special):
        self.pass_len = pass_len
        self.max_upper = max_upper
        self.special = special
        self.char_array = []
        self.password = ''
        self.check()


    def __str__(self):
        return self.password

    def __repr__(self):
        return self.password

    def __add__(self, other):
        return self.password + other.password



