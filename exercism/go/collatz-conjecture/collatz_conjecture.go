package collatzconjecture

import (
	"errors"
)

// CollatzConjecture calculates the number of steps required to reach 1
// More information here: https://en.wikipedia.org/wiki/Collatz_conjecture
func CollatzConjecture(start int) (int, error) {

	if start < 1 {
		return -1, errors.New("Starting value is below 1")
	}

	steps := 0

	for {

		if start == 1 {
			return steps, nil
		} else {
			if start%2 == 0 {
				start = start / 2
			} else {
				start = 3*start + 1
			}
		}

		steps += 1

	}

}
