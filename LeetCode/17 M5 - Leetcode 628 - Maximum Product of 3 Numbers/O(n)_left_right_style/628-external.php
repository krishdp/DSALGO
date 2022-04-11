// https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/

<?php
// A PHP program to find a maximum product of a triplet
// in array of integers

/* Function to find a maximum product of a triplet
in array of integers of size n */
function maxProduct($arr, $n)
{
	// if size is less than 3, no triplet exists
	if ($n < 3)
		return -1;

	// Construct four auxiliary vectors
	// of size n and initialize them by -1
	$leftMin=array_fill(0,$n, -1);
	$rightMin=array_fill(0,$n, -1);
	$leftMax=array_fill(0,$n, -1);
	$rightMax=array_fill(0,$n, -1);

	// will contain max product
	$max_product = PHP_INT_MIN;

	// to store maximum element on left of array
	$max_sum = $arr[0];

	// to store minimum element on left of array
	$min_sum = $arr[0];

	// leftMax[i] will contain max element
	// on left of arr[i] excluding arr[i].
	// leftMin[i] will contain min element
	// on left of arr[i] excluding arr[i].
	for ($i = 1; $i < $n; $i++)
	{
		$leftMax[$i] = $max_sum;
		if ($arr[$i] > $max_sum)
			$max_sum = $arr[$i];

		$leftMin[$i] = $min_sum;
		if ($arr[$i] < $min_sum)
			$min_sum = $arr[$i];
	}

	// reset max_sum to store maximum element on
	// right of array
	$max_sum = $arr[$n - 1];

	// reset min_sum to store minimum element on
	// right of array
	$min_sum = $arr[$n - 1];

	// rightMax[i] will contain max element
	// on right of arr[i] excluding arr[i].
	// rightMin[i] will contain min element
	// on right of arr[i] excluding arr[i].
	for ($j = $n - 2; $j >= 0; $j--)
	{
		$rightMax[$j] = $max_sum;
		if ($arr[$j] > $max_sum)
			$max_sum = $arr[$j];

		$rightMin[$j] = $min_sum;
		if ($arr[$j] < $min_sum)
			$min_sum = $arr[$j];
	}

	// For all array indexes i except first and
	// last, compute maximum of arr[i]*x*y where
	// x can be leftMax[i] or leftMin[i] and
	// y can be rightMax[i] or rightMin[i].
	for ($i = 1; $i < $n - 1; $i++)
	{
		$max1 = max($arr[$i] * $leftMax[$i] * $rightMax[$i],
					$arr[$i] * $leftMin[$i] * $rightMin[$i]);

		$max2 = max($arr[$i] * $leftMax[$i] * $rightMin[$i],
					$arr[$i] * $leftMin[$i] * $rightMax[$i]);

		$max_product = max($max_product, max($max1, $max2));
	}

	return $max_product;
}

// Driver program to test above functions
	$arr = array( 1, 4, 3, -6, -7, 0 );
	$n = count($arr);

	$max = maxProduct($arr, $n);

	if ($max == -1)
		echo "No Triplet Exists";
	else
		echo "Maximum product is ".$max;


// This code is contributed by mits
?>
