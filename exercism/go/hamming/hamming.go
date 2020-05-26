package hamming

import (
	e "errors"
)

func Distance(a, b string) (int, error) {

	if len(a) != len(b) {
		return -1, e.New("Strings are not equal")
	}

	count := 0

	for i, _ := range a {
		if a[i] != b[i] {
			count += 1
		}
	}

	return count, nil

}
