// https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/ 


// C# program to find a maximum product of a
// triplet in array of integers
using System;
public class GFG {
 
    /* Function to find a maximum product of a triplet
in array of integers of size n */
    static int maxProduct(int []arr, int n) {
        // if size is less than 3, no triplet exists
        if (n < 3) {
            return -1;
        }
 
        // Sort the array in ascending order
        Array.Sort(arr);
 
        // Return the maximum of product of last three
        // elements and product of first two elements
        // and last element
        return Math.Max(arr[0] * arr[1] * arr[n - 1],
                arr[n - 1] * arr[n - 2] * arr[n - 3]);
    }
 
// Driver program to test above functions
    public static void Main() {
        int []arr = {-10, -3, 5, 6, -20};
        int n = arr.Length;
 
        int max = maxProduct(arr, n);
 
        if (max == -1) {
            Console.WriteLine("No Triplet Exists");
        } else {
            Console.WriteLine("Maximum product is " + max);
        }
 
    }
}
// This code is contributed by 29AjayKumar
