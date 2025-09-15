import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __add__(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __mul__(self, escalar):
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    def producto_vectorial(self, otro):
        x_comp = self.y * otro.z - self.z * otro.y
        y_comp = self.z * otro.x - self.x * otro.z
        z_comp = self.x * otro.y - self.y * otro.x
        return Vector3D(x_comp, y_comp, z_comp)
    def normal(self):
        magnitud = abs(self)
        if magnitud == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / magnitud, self.y / magnitud, self.z / magnitud)
if __name__ == "__main__":
    print("--- Operaciones Vectoriales con Sobrecarga ---")
    print("\nIngrese las componentes del primer vector (a):")
    a_x = float(input("Componente x: "))
    a_y = float(input("Componente y: "))
    a_z = float(input("Componente z: "))
    a = Vector3D(a_x, a_y, a_z)
    print("\nIngrese las componentes del segundo vector (b):")
    b_x = float(input("Componente x: "))
    b_y = float(input("Componente y: "))
    b_z = float(input("Componente z: "))
    b = Vector3D(b_x, b_y, b_z)
    escalar = float(input("\nIngrese un valor escalar (r): "))
    print(f"\nOperaciones para a={a}, b={b} y r={escalar}:")
    print("-" * 40)
    print(f"a) Suma (a + b): {a + b}")
    print(f"b) Multiplicación por escalar (r * a): {escalar * a}")
    print(f"c) Longitud de a (|a|): {abs(a):.4f}")
    print(f"d) Normal de a (a / |a|): {a.normal()}")
    print(f"e) Producto escalar (a · b): {a.producto_escalar(b)}")
    print(f"f) Producto vectorial (a x b): {a.producto_vectorial(b)}")