class Negator:
    @staticmethod
    def neg(n):
        if isinstance(n, bool):
            return not n
        elif isinstance(n, (int, float)):
            return -n
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

print(Negator.neg(6))
print(Negator.neg(False))