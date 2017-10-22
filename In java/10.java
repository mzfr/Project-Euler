// problem 10:
// sum of prime number under 2000000

package euler10;

public class Euler10 {

    public static void main(String[] args) {

        int num = 0;

       double primenumbers = 0;
        for (int i = 1;i<=2000000;i++)
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
            primenumbers = primenumbers + i;
        }
        System.out.println("The sum of the prime numbers under 2000000 is : " + primenumbers);
    }
}

// The algorithm to find prime numbers can be developed to make the algorithm work faster
