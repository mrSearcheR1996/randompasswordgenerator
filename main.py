#add module and library
from abc import ABC,abstractmethod
import string
from random import choices

class PasswordGen(ABC):

    @abstractmethod
    def password_generator(self):
        pass
#ABC abstract class
class AlfabetPasswordGen(PasswordGen):
    def __init__(self,lenght):
        self.lenght=lenght

    #abstractmethod function
    def password_generator(self):
        return ''.join(choices(string.ascii_letters,k=self.lenght))

#add varobale as class im use 35 for 35 character password lenght
alfapassword=AlfabetPasswordGen(35)
print(alfapassword.password_generator())