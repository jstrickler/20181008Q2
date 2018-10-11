#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class SpamBase(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass



class ClassicSpam(SpamBase):
    def read(self):
        pass
    def write(self):
        pass

    @property
    def last_name(self):
        return




class SpamLite(SpamBase):
    def read(self):
        pass
    def write(self):
        pass



cs = ClassicSpam()
sl = SpamLite()



