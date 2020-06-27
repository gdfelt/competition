package luhn

import "strings"

// Valid calculates whether a given number is valid per the Luhn algorithm
// Algorithm documented here: https://en.wikipedia.org/wiki/Luhn_algorithm#Pseudocode_implementation
func Valid(ccNumber string) bool {
	newString := strings.ReplaceAll(ccNumber, " ", "")

	nDigits := len(newString)
	sum := int(newString[nDigits-1]) - '0'
	parity := nDigits % 2

	if nDigits < 2 {
		return false
	}

	for i := 0; i < nDigits-1; i++ {
		digit := int(newString[i] - '0')
		if digit < 0 || digit > 9 {
			return false
		}
		if i%2 == parity {
			digit *= 2
		}
		if digit > 9 {
			digit -= 9
		}
		sum += digit
	}

	return sum%10 == 0
}
