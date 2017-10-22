// Problem 6
// Find the difference between the sum of the squares of the first one
// hundred natural numbers and the square of the sum.

package euler6;

import java.math.*;
public class Euler6 {

    public static void main(String[] args) {
        int sos = 0;
        int sqos = 0;
        int sum  = 0;
        for(int i = 1;i<=100;i++)
        {
            // finiding the sum of the square
            int power = (int) Math.pow(i,2);
            sos = power + sos;

             sum = i + sum;
        }
        sqos = (int) Math.pow(sum,2); // finding square of the sum
        int diff = sqos - sos;
        System.out.println("The difference between the sum of the square and the square of sum: " + diff);

    }
}
