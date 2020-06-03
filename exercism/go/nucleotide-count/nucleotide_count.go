// Package dna produces a histogram of valid nucleotides
package dna

import (
	"errors"
)

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[int32]int

// DNA is a list of nucleotides.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
// Returns an error if d contains an invalid nucleotide.
func (d DNA) Counts() (Histogram, error) {
	var h Histogram = map[int32]int{'A': 0, 'C': 0, 'G': 0, 'T': 0}

	for _, c := range d {
		if c == 'A' || c == 'C' || c == 'G' || c == 'T' {
			h[c] = h[c] + 1
		} else {
			return nil, errors.New("Invalid nucleotide detected")
		}
	}

	return h, nil
}
