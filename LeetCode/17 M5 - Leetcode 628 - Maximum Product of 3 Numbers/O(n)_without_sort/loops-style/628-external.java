// src https://www.techiedelight.com/find-triplet-maximum-product-array/


class Main
{
    // Find a triplet having the maximum product in an array
    public static void printTriplet(int[] A)
    {
        int n = A.length;
 
        // invalid input
        if (n <= 2) {
            System.out.print("No triplet exists. The array has less than 3 elements.");
        }
 
        // 1. Find the index of the largest, second largest, and third largest
        // array element
        int max_index1 = 0, max_index2 = -1, max_index3 = -1;
        for (int i = 1; i < n; i++)
        {
            // if the current element is less than the largest element found so far
            if (A[i] > A[max_index1])
            {
                max_index3 = max_index2;
                max_index2 = max_index1;
                max_index1 = i;
            }
 
            // if the current element is less than the second largest element
            // found so far
            else if (max_index2 == -1 || A[i] > A[max_index2])
            {
                max_index3 = max_index2;
                max_index2 = i;
            }
 
            // if the current element is less than the third largest element
            // found so far
            else if (max_index3 == -1 || A[i] > A[max_index3]) {
                max_index3 = i;
            }
        }
 
        // 2. Find the index of the smallest and second smallest array element
        int min_index1 = 0, min_index2 = -1;
        for (int i = 1; i < n; i++)
        {
            // if the current element is more than the smallest element found so far
            if (A[i] < A[min_index1])
            {
                min_index2 = min_index1;
                min_index1 = i;
            }
            // if the current element is more than the second smallest element
            // found so far
            else if (min_index2 == -1 || A[i] < A[min_index2]) {
                min_index2 = i;
            }
        }
 
        if (A[max_index1] * A[max_index2] * A[max_index3] >
                A[min_index1] * A[min_index2] * A[max_index1]) {
            System.out.print("Triplet is (" + A[max_index1] + ", " + A[max_index2]
                                + ", " + A[max_index3] + ")");
        }
        else {
            System.out.print("Triplet is (" + A[min_index1] + ", " + A[min_index2]
                                + ", " + A[max_index1] + ")");
        }
    }
 
    public static void main(String[] args)
    {
        int[] A = { -4, 1, -8, 9, 6 };
        printTriplet(A);
    }
}
