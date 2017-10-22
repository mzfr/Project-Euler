// Problem 16
// What is the sum of the digits of the number 2^1000?


package euler16;

import java.math.*;
public class Euler16 {


    public static void main(String[] args) {
           int power =  (int) Math.pow(2,1000);
           System.out.println(power);
           int length = String.valueOf(power).length();
           int sum = 0;
           for (int i =1;i<=length ;i++)
           {
               int digit =  power%10;
               sum = sum + digit;
               power = power/10;
           }
           System.out.println("the sum of the digits of the number 2^1000 is : " + sum);
    }
}

