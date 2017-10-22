// problem No. 7

// Find 10001 position prime Numbers

package euler7;

public class Euler7 {

    public static void main(String[] args) {

   int num = 0;
   int primeno[];
   primeno = new int [100];
       double primenumbers = 0;
        for (int i = 1;i<=100;i++)
        {
        int counter = 0;
            for (num = i;num>=1;num--)
            {
                if (i%num == 0)
                {
                    counter  = counter + 1;
                }
                }
        if (counter == 2)
        {
            for (int m = 0 ; m < 100;m++)
            {
                primeno[m] = i;
            }
            }
            }
        System.out.println("the prime number on 100 position is : " + primeno[0]);
}
}

// The algorithm to find prime numbers can be developed to make the algorithm work faster
