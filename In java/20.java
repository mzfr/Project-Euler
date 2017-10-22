// problem 20
//  Find the sum of the digits in the number 100!
package euler20;

public class Euler20 {


    public static void main(String[] args) {

          int factorial = 100;
          int sum =0;
          // Function to find the factorial of 100
          for (int i = 100;i>=1;i--)
          {
              factorial = i * factorial ;
          }
          System.out.println("The factorial of 100 is : " + factorial);

             //
             int length = String.valueOf(factorial).length();
              for (int i =1;i<=length ;i++)
           {
               int digit =  factorial%10;
               sum = sum + digit;
               power = factorial/10;
           }
           System.out.println("the sum of the digits of the number 2^1000 is : " + sum);
    }
}
