from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        if horizontal in ["a", "b", "c", "d", "f", "g", "h"]:
            self.horizontal = horizontal
        if vertical in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass

class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        if horizontal in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.horizontal = horizontal
        if vertical in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.vertical = vertical

    def can_move(self, horizontal, vertical):
        correct = True
        if horizontal in ["a", "b", "c", "d", "e", "f", "g", "h"] and vertical in [1, 2, 3, 4, 5, 6, 7, 8]:
            if not (ord(self.horizontal)-1 <= ord(horizontal) <= ord(self.horizontal)+1):
                correct = False
            if not(self.vertical-1 <= vertical <= self.vertical+1):
                correct = False
        return correct

class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        if horizontal in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.horizontal = horizontal
        if vertical in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.vertical = vertical

    def can_move(self, horizontal, vertical):
        correct = False
        if horizontal in ["a", "b", "c", "d", "e", "f", "g", "h"] and vertical in [1, 2, 3, 4, 5, 6, 7, 8]:
            if ord(self.horizontal) - 2 == ord(horizontal) or ord(self.horizontal) + 2 == ord(horizontal):
                if self.vertical - 1 == vertical or self.vertical + 1 == vertical:
                    print(1)
                    correct = True

            elif self.vertical - 2 == vertical or self.vertical + 2 == vertical:
                if ord(self.horizontal) - 1 == ord(horizontal) or ord(self.horizontal) + 1 == ord(horizontal):
                    print(3)
                    correct = True

        return correct



king = King("f", 3)
print(king.can_move("g", 4))

knight = Knight("e", 4)
print(knight.can_move("f", 2))