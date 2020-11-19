package sieve

import (
	"math"
)

// Sieve function caluculates the Sieve of Eratosthenes
func Sieve(limit int) []int {

	if limit < 2 {
		return make([]int, 0)
	}

	if limit == 2 {
		return []int{2}
	}

	sieve := make([]bool, limit+1)
	for i := range sieve {
		sieve[i] = true
	}
	sieve[0] = false
	sieve[1] = false

	// start sieve operation
	root := int(math.Sqrt(float64(limit)))
	for i := 2; i <= root; i++ {
		if sieve[i] {
			for n := i * i; n < limit+1; n += i {
				sieve[n] = false
			}
		}
	}

	ret := make([]int, 0)

	for i, s := range sieve {
		if s {
			ret = append(ret, i)
		}
	}

	return ret

}
