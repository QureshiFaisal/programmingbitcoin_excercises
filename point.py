class Point:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x is None and self.y is None:
            return
        # if self.y**2 != self.x**3 + a * self.x + b:
        #     raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            # Point doubling
            s = (3 * self.x**2 + self.a) * (2 * self.y).__pow__(-1)
        else:
            # Point addition
            s = (other.y - self.y) * (other.x - self.x).__pow__(-1)
        
        x = (s**2 - self.x - other.x)
        y = (s * (self.x - x) - self.y)
        
        return self.__class__(x, y, self.a, self.b)

    def __repr__(self):
        return 'Point({}, {}, {}, {})'.format(self.x, self.y, self.a, self.b)
