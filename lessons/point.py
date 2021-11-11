"""Example of a Point Class."""
from __future__ import annotations


class Point: 
    x: float
    y: float

    def __init__(self, x: float, y: float): 
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y
    
    def scale_by(self, factor: float) -> None: 
        """Mutates: multiplies components by factor."""
        # Modifies object it is called on
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        # Sets up brand new object, assign it values and returns new object back
        # Easier to understand rather than trying to figure out how it changed your object
        x: float = self.x * factor
        y: float = self.y * factor
        p: Point = Point(x, y)
        return p

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str: 
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"


p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)