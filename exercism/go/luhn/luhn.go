package luhn

import "strings"

// Valid calculates whether a given number is valid per the Luhn algorithm
// Algorithm documented here: https://en.wikipedia.org/wiki/Luhn_algorithm#Pseudocode_implementation
func Valid(ccNumber string) bool {
	newString := strings.ReplaceAll(ccNumber, " ", "")
	sum := 0
	parity := len(newString)%2 == 0
	if len(newString) < 2 {
		return false
	}
	for _, r := range newString {
		digit := int(r - '0')
		if digit < 0 || digit > 9 {
			return false
		}
		if parity {
			digit *= 2
		}
		if digit > 9 {
			digit -= 9
		}
		sum += digit
		parity = !parity
	}
	return sum%10 == 0
}
