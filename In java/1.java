// problem 1

// Add all the natural numbers below one thousand that are multiples of 3 or 5.

public class Euler1 {

     public static void main(String[] args) {

    int add = 0;
        for (int i = 1; i<= 1000 ; i++)
    {
        if ((i%3==0)&&(i%5==0))
        {
             add = add + i ;
        }
        }
         System.out.println("The sum of the natural numbers below 1000 that are multiples of 3 and 5 is : " + add);
    }
}
