// https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/


// Java program to find a maximum product of a
// triplet in array of integers
 
import java.util.Arrays;
 
class GFG {
 
    /* Function to find a maximum product of a triplet
   in array of integers of size n */
    static int maxProduct(int arr[], int n) {
        // if size is less than 3, no triplet exists
        if (n < 3) {
            return -1;
        }
 
        // Sort the array in ascending order
        Arrays.sort(arr);
 
        // Return the maximum of product of last three
        // elements and product of first two elements
        // and last element
        return Math.max(arr[0] * arr[1] * arr[n - 1],
                arr[n - 1] * arr[n - 2] * arr[n - 3]);
    }
 
// Driver program to test above functions
    public static void main(String[] args) {
        int arr[] = {-10, -3, 5, 6, -20};
        int n = arr.length;
 
        int max = maxProduct(arr, n);
 
        if (max == -1) {
            System.out.println("No Triplet Exists");
        } else {
            System.out.println("Maximum product is " + max);
        }
 
    }
}
/* This Java code is contributed by Rajput-Ji*/
