// https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/


<?php
// PHP program to find a maximum product of a
// triplet in array of integers

/* Function to find a maximum product of a triplet
in array of integers of size n */
	function maxProduct($arr, $n)
	
	// if size is less than 3, no triplet exists
	{
		if ($n < 3)
		{
			return -1;
		}

		// Sort the array in ascending order
		sort($arr);

		// Return the maximum of product of last three
		// elements and product of first two elements
		// and last element
		return max($arr[0] * $arr[1] * $arr[$n - 1],
				$arr[$n - 1] * $arr[$n - 2] * $arr[$n - 3]);
	}

	// Driver code
	$arr = array(-10, -3, 5, 6, -20);
	$n = sizeof($arr);

	$max = maxProduct($arr, $n);

	if ($max == -1)
	{
		echo("No Triplet Exists");
	}
	else
	{
		echo("Maximum product is " . $max);
	}


/* This code is contributed by Code_Mech*/
