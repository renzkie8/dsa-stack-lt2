public class Renz {
  
  public static void main(String[] args) {
    
    

    Integer Num1 = 5;
    Integer Num2 = 7;
    Integer temp;

    temp = Num2;
    Num2 = Num1;
    Num1 =temp;

    temp = Num1;
    Num1 = Num2;
    Num2 = temp;

    System.out.println("Before Swap");
    System.out.println("Num1="  +" " + Num1);
    System.out.println("Num2="  +" " + Num2);
    System.out.println("After Swap");
    System.out.println("Num2="  +" " + Num2);
    System.out.println("Num1="  +" " + Num1);
  }
}
