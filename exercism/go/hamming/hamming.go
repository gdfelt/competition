package hamming

import (
	e "errors"
)

// Distance calculates the hamming distance between two DNA strings
func Distance(a, b string) (int, error) {

	if len(a) != len(b) {
		return -1, e.New("Strings are not equal")
	}

	count := 0

	for i := range a {
		if a[i] != b[i] {
			count++
		}
	}

	return count, nil

}
