import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        return Vector3D(scalar * self.x, scalar * self.y, scalar * self.z)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError(" ")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    a = Vector3D(2, 5, 0)
    b = Vector3D(4, 10, 0)

    print(f"a: {a}, b: {b}")
    print(f"Suma: {a + b}")
    print(f"Multiplicación por escalar (2 * a): {a * 2}")
    print(f"Longitud de a: {a.magnitude()}")
    print(f"Normal de a: {a.normalize()}")
    print(f"Producto escalar (a · b): {a.dot(b)}")
    print(f"Producto vectorial (a × b): {a.cross(b)}")