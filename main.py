#add module and library
from abc import ABC,abstractmethod
import string
from random import choices

class PasswordGen:

    @abstractmethod
    def password_generator(self):
        pass
