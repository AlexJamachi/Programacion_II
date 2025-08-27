package Ej1_Ecuacion_Lineal_2x2;
public class EcuacionLineal {
    private double a, b, c, d, e, f;
    public EcuacionLineal(double a, double b, double c, double d, double e, double f) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.e = e;
        this.f = f;
    }
    public boolean tieneSolucion() {
        return (a * d - b * c) != 0;
    }
<<<<<<< HEAD
    public double obtenerX() {
        return (e * d - b * f) / (a * d - b * c);
    }
    public double obtenerY() {
=======
    public double getX() {
        return (e * d - b * f) / (a * d - b * c);
    }
    public double getY() {
>>>>>>> 51710fa3fd02d4ba657c05d48f1ae2fd49b8b848
        return (a * f - e * c) / (a * d - b * c);
    }
}