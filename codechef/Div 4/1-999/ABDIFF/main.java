import java.util.Scanner;
import java.lang.Math;

class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int result = Math.abs(((a + b) - (a * b)));
        System.out.println(result);

        scanner.close();
    }
}