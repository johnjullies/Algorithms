// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-21-generics

class Printer
{
   public static < E > void printArray( E[] inputArray )
   {           
         for ( E element : inputArray ){        
            System.out.println( element );
         }
    }
}
