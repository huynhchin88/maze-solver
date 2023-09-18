#16 possible patterns, represent the total possibility using bits
#Border Sides   Bit String   Bit Count   Decimal Value
#               0000         0           0
#N              0001         1           1
#S              0010         1           2
#W              0100         1           4
#E              1000         1           8
#NS             0011         2           3
#NW             0101         2           5
#NE             1001         2           9
#SW             0110         2           6
#SE             1010         2           10
#WE             1100         2           12
#NSW            0111         3           7
#NSE            1011         3           11
#NWE            1101         3           13
#SWE            1110         3           14
#NSWE           1111         4           15

from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        return self in (self.TOP | self.LEFT,
                        self.TOP | self.RIGHT,
                        self.BOTTOM | self.LEFT,
                        self.BOTTOM | self.RIGHT)

    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3
    
    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2