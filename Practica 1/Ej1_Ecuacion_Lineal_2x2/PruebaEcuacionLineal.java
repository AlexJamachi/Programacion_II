package Ej1_Ecuacion_Lineal_2x2;
import java.util.Scanner;
public class PruebaEcuacionLineal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese a, b, c, d, e, f: ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        double d = scanner.nextDouble();
        double e = scanner.nextDouble();
        double f = scanner.nextDouble();
        EcuacionLineal ecuacion = new EcuacionLineal(a, b, c, d, e, f);
        if (ecuacion.tieneSolucion()) {
            System.out.println("x = " + ecuacion.obtenerX() + ", y = " + ecuacion.obtenerY());
        } else {
            System.out.println("La ecuación no tiene solución");
        }
        scanner.close();
    }
}