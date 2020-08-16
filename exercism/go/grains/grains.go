package grains

import (
	"errors"
	"math"
)

func Total() uint64 {
	var total uint64 = 0
	for i := 1; i < 65; i++ {
		square, _ := Square(i)
		total += square
	}
	return total
}

func Square(num int) (uint64, error) {
	if num < 1 || num > 64 {
		return 0, errors.New("Cannot be less than 1 or greater than 64")
	}
	return uint64(math.Pow(2, float64(num-1))), nil
}
