package scrabble

import (
	"fmt"
	"strings"
)

// Score takes a Scabble word and calculates the score
func Score(word string) int {

	score := 0

	for _, c := range strings.ToLower(word) {

		switch c {
		case 'a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't':
			score++
		case 'd', 'g':
			score += 2
		case 'b', 'c', 'm', 'p':
			score += 3
		case 'f', 'h', 'v', 'w', 'y':
			score += 4
		case 'k':
			score += 5
		case 'j', 'x':
			score += 8
		case 'q', 'z':
			score += 10
		default:
			fmt.Println("Bad character: ", c)
		}
	}

	return score
}
