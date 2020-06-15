package diffsquares

import (
	"math"
)

// SquareOfSum calculates the square of the sum from 1 to the provided number
func SquareOfSum(number int) int {

	// Formula found here: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
	return int(math.Pow(float64(number*(number+1)/2), 2))
}

// SumOfSquares calculates the sum of the squares from 1 to the provided number
func SumOfSquares(number int) int {

	// Formula found here: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
	return number * (number + 1) * (2*number + 1) / 6
}

// Difference calculates the difference between SquareOfSum() and SumOfSquares()
func Difference(number int) int {
	return SquareOfSum(number) - SumOfSquares(number)
}
