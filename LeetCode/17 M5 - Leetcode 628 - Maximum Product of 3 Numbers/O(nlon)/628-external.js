// https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/

<script>

// Javascript program to find a maximum
// product of a triplet in array of integers

// Function to find a maximum product of a
// triplet in array of integers of size n
function maxProduct(arr, n)
{
	
	// If size is less than 3, no
	// triplet exists
	if (n < 3)
	{
		return -1;
	}

	// Sort the array in ascending order
	arr.sort();

	// Return the maximum of product of last three
	// elements and product of first two elements
	// and last element
	return Math.max(arr[0] * arr[1] * arr[n - 1],
			arr[n - 1] * arr[n - 2] * arr[n - 3]);
}

// Driver code
var arr = [-10, -3, 5, 6, -20];
var n = arr.length;
var max = maxProduct(arr, n);

if (max == -1)
{
	document.write("No Triplet Exists");
}
else
{
	document.write("Maximum product is " + max);
}

// This code is contributed by Rajput-Ji

</script>
