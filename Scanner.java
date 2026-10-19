import java.util.Scanner;

public class Scanner{

  public static void main(String[]args) {

    Scanner scanner = new Scanner(System.in);

     String enterNum1 = scanner.nextLine();
        System.out.println("You entered the first number: " + enterNum1);

        scanner.close();
  }
}