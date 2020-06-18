package isogram

import (
	"strings"
)

// IsIsogram calculates whether a given string is an isogram or not
func IsIsogram(phrase string) bool {
	lowerPhrase := strings.ToLower(phrase)
	for _, c := range phrase {
		if strings.Count(lowerPhrase, string(c)) != 1 && 'a' <= c && c <= 'z' {
			return false
		}
	}

	return true
}
