
package Personal;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] histogram = new int[10];
        
        System.out.println("Ingrese la cantidad de asteriscos para cada valor (0 al 9):");
        for (int i = 0; i < 10; i++) {
            System.out.print("Element " + i + ": ");
            int asterisks = scanner.nextInt();
            histogram[i] = asterisks;
        }
        
        // Display the histogram
        System.out.println("\nElement | Value | Histogram");
        System.out.println("--------------------------");
        for (int i = 0; i < 10; i++) {
            System.out.printf("%7d | %5d | ", i, histogram[i]);
            for (int j = 0; j < histogram[i]; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}

