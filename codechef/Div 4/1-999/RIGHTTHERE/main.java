import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
         int n = Integer.parseInt(scanner.nextLine());

         while(n != 0){
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            if((b > a) || (a == b)){
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
            n -= 1;
         }

        scanner.close();
    }
}