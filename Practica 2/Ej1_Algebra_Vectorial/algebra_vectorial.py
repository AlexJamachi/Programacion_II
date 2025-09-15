import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def sumar(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def restar(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    def producto_vectorial(self, otro):
        x_comp = self.y * otro.z - self.z * otro.y
        y_comp = self.z * otro.x - self.x * otro.z
        z_comp = self.x * otro.y - self.y * otro.x
        return Vector(x_comp, y_comp, z_comp)
    def multiplicar_por_escalar(self, r):
        return Vector(self.x * r, self.y * r, self.z * r)
class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def son_perpendiculares_v1(self):
        magnitud_suma = self.a.sumar(self.b).magnitud()
        magnitud_resta = self.a.restar(self.b).magnitud()
        return math.isclose(magnitud_suma, magnitud_resta)
    def son_perpendiculares_v2(self):
        magnitud_a_menos_b = self.a.restar(self.b).magnitud()
        magnitud_b_menos_a = self.b.restar(self.a).magnitud()
        return math.isclose(magnitud_a_menos_b, magnitud_b_menos_a)
    def son_perpendiculares_v3(self):
        return math.isclose(self.a.producto_escalar(self.b), 0)
    def son_perpendiculares_v4(self):
        magnitud_suma_sq = self.a.sumar(self.b).magnitud() ** 2
        magnitud_a_sq = self.a.magnitud() ** 2
        magnitud_b_sq = self.b.magnitud() ** 2
        return math.isclose(magnitud_suma_sq, magnitud_a_sq + magnitud_b_sq)
    def son_paralelos_v1(self):
        try:
            if self.b.x == 0 and self.b.y == 0 and self.b.z == 0:
                return self.a.x == 0 and self.a.y == 0 and self.a.z == 0
            r_list = []
            if self.b.x != 0: r_list.append(self.a.x / self.b.x)
            if self.b.y != 0: r_list.append(self.a.y / self.b.y)
            if self.b.z != 0: r_list.append(self.a.z / self.b.z)
            if not r_list: return False
            first_r = r_list[0]
            for r in r_list:
                if not math.isclose(r, first_r):
                    return False
            return True
        except ZeroDivisionError:
            return False
    def son_paralelos_v2(self):
        producto = self.a.producto_vectorial(self.b)
        return math.isclose(producto.magnitud(), 0)
    def proyeccion_a_sobre_b(self):
        producto_escalar = self.a.producto_escalar(self.b)
        magnitud_b_sq = self.b.magnitud() ** 2
        if magnitud_b_sq == 0:
            return Vector(0, 0, 0)
        escalar = producto_escalar / magnitud_b_sq
        return self.b.multiplicar_por_escalar(escalar)
    def componente_a_en_b(self):
        producto_escalar = self.a.producto_escalar(self.b)
        magnitud_b = self.b.magnitud()
        if magnitud_b == 0:
            return 0
        return producto_escalar / magnitud_b
if __name__ == "__main__":
    print("--- Calculadora de Álgebra Vectorial ---")
    print("\nIngrese las componentes del primer vector (a):")
    a_x = float(input("Componente x: "))
    a_y = float(input("Componente y: "))
    a_z = float(input("Componente z: "))
    vector_a = Vector(a_x, a_y, a_z)
    print("\nIngrese las componentes del segundo vector (b):")
    b_x = float(input("Componente x: "))
    b_y = float(input("Componente y: "))
    b_z = float(input("Componente z: "))
    vector_b = Vector(b_x, b_y, b_z)
    calculadora = AlgebraVectorial(vector_a, vector_b)
    print(f"\nResultados para a={vector_a} y b={vector_b}:")
    print("-" * 30)
    print("¿Son perpendiculares?")
    print(f"  a) Según |a+b| = |a-b|: {calculadora.son_perpendiculares_v1()}")
    print(f"  b) Según |a-b| = |b-a|: {calculadora.son_perpendiculares_v2()}")
    print(f"  c) Según a·b = 0: {calculadora.son_perpendiculares_v3()}")
    print(f"  d) Según |a+b|² = |a|² + |b|²: {calculadora.son_perpendiculares_v4()}")
    print("\n¿Son paralelos?")
    print(f"  e) Según a = rb: {calculadora.son_paralelos_v1()}")
    print(f"  f) Según a x b = 0: {calculadora.son_paralelos_v2()}")
    print("\nProyección y Componente:")
    print(f"  g) Proyección de a sobre b: {calculadora.proyeccion_a_sobre_b()}")
    print(f"  h) Componente de a en b: {calculadora.componente_a_en_b():.4f}")