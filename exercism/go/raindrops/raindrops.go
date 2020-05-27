package raindrops

import (
	"strconv"
)

// Convert produces a 'Raindrop' string based on the factors of the number provided
func Convert(number int) string {

	result := ""
	if number%3 == 0 {
		result += "Pling"
	}

	if number%5 == 0 {
		result += "Plang"
	}

	if number%7 == 0 {
		result += "Plong"
	}

	if result == "" {
		return strconv.Itoa(number)
	}
	return result

}
