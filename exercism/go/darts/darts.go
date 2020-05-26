package darts

import "math"

// Score funct
func Score(x float64, y float64) int {

	dist := math.Abs(math.Sqrt(x*x + y*y))

	if dist <= 1 {
		return 10
	} else if dist <= 5 {
		return 5
	} else if dist <= 10 {
		return 1
	}
	return 0

}
