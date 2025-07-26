from rich.console import Console
from string import ascii_lowercase, ascii_uppercase
from random import choice, shuffle

from config import PageText

# * Creation of class objects
console = Console()
pagetxt = PageText()

class PassGen:
    def params(self):
        self.alphabet_upper = ascii_uppercase
        self.alphabet_lower = ascii_lowercase
        self.nums = '1234567890'
        self.symbols = '!?/,._-+*%$#&()[]<>~'
        self.password = ''

    def generation(self):
        # * Adding 4 small letters
        for alpL in range(4):
            ran_alp_low = choice(self.alphabet_lower)
            self.password += ran_alp_low
                
        # * Adding 2 large letters
        for alpU in range(2):
            ran_alp_up = choice(self.alphabet_upper)
            self.password += ran_alp_up
                
        # * Adding 4 digits
        for nms in range(4):
            ran_nums = choice(self.nums)
            self.password += ran_nums
            
        # * Adding 2 special characters
        for symb in range(2):
            ran_symb = choice(self.symbols)
            self.password += ran_symb

        # * Transformation into list and mixing elements
        self.pass_list = list(self.password)
        shuffle(self.pass_list)

    def outputPassword(self):
        pagetxt.titlePassGen()
        result = ''.join(self.pass_list)

        console.print(f"[bold yellow]Password: [/]{result}")