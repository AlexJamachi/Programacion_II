package Ej3_Estadisticas.Programacion_Modular;
import java.util.Scanner;
public class EstadisticaModular {
    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }
    public static double desviacion(double[] numeros) {
        double media = promedio(numeros);
        double sumaCuadrados = 0;
        for (double num : numeros) {
            sumaCuadrados += Math.pow(num - media, 2);
        }
        return Math.sqrt(sumaCuadrados / (numeros.length - 1));
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] datos = new double[10];
        System.out.println("Ingrese 10 números:");
        for (int i = 0; i < 10; i++) {
            datos[i] = scanner.nextDouble();
        }
        double media = promedio(datos);
        double desv = desviacion(datos);
        System.out.printf("El promedio es %.2f\n", media);
        System.out.printf("La desviación estandard es %.5f\n", desv);
        scanner.close();
    }
}