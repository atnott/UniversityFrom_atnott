class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstname = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            return "10000р"
        elif self.averageMark > 3:
            return "5000р"
        else:
            return "0р"

class Undergraduate(Bachelor):
    def getScholarship(self):
        if self.averageMark == 5:
            return "15000р"
        elif self.averageMark > 3:
            return "7500р"
        else:
            return "0р"

b1 = Bachelor('Андрей', 'Смоленцев', '14122', 4)
b2 = Bachelor('Иван', 'Сидоров', '14344', 5)
m1 = Undergraduate('Сергей', 'Лагучев', '14566', 3)
m2 = Undergraduate('Антон', 'Кротов', '14121', 4)

l = [b1, b2, m1, m2]

for i in l:
    print(f"Стипендия ({i.lastName}): {i.getScholarship()}")