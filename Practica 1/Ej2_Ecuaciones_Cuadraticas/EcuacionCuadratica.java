package Ej2_Ecuaciones_Cuadraticas;
public class EcuacionCuadratica {
    private double a, b, c;
    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public double obtenerDiscriminante() {
        return b * b - 4 * a * c;
    }
    public double obtenerRaiz1() {
        if (obtenerDiscriminante() >= 0) {
            return (-b + Math.sqrt(obtenerDiscriminante())) / (2 * a);
        } else {
            return 0;
        }
    }
    public double obtenerRaiz2() {
        if (obtenerDiscriminante() >= 0) {
            return (-b - Math.sqrt(obtenerDiscriminante())) / (2 * a);
        } else {
            return 0;
        }
    }
}
