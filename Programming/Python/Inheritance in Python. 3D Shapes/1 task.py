class Counter:
    def __init__(self, start = 0):
        self.value = start

    def inc(self, x = 1):
        if isinstance(x, int):
            self.value += x

    def dec(self, x = 1):
        if isinstance(x, int):
            if x > self.value:
                self.value = 0
            else:
                self.value -= x

class NonDecCounter(Counter):
    def dec(self, x = 1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start = 0, limit = 10):
        super().__init__(start)
        self.limit = limit

    def inc(self, x = 1):
        if isinstance(x, int):
            if (x+self.value) > self.limit:
                self.value = self.limit
            else:
                self.value += x


c = Counter(3)

c.dec(2)
print(c.value)

ndc = NonDecCounter(7)

ndc.dec(5)
print(ndc.value)

lc = LimitedCounter(2)

lc.inc(10)
print(lc.value)