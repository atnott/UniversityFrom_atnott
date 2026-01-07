from abc import ABC, abstractmethod

class Date(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return f"{self.year}-{self.month}-{self.day}"

class USADate(Date):
    def format(self):
        return f"{self.month}-{self.day}-{self.year}"

class ItalianDate(Date):
    def format(self):
        return f"{self.day}/{self.month}/{self.year}"

i = ItalianDate("2007", "02", "20")
u = USADate("2007", "02", "20")
print(i.format(), u.format())
