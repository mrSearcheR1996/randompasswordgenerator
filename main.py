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

    def password_generator(self):
        return ''.join(choices(string.ascii_letters,k=self.lenght))


alfapassword=AlfabetPasswordGen(35)
print(alfapassword.password_generator())