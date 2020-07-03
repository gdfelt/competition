// Package triangle determines whether given side lengths can form a triangle or not
package triangle

import "math"

type Kind string

const (
	NaT Kind = "nat" // not a triangle
	Equ Kind = "equ" // equilateral
	Iso Kind = "iso" // isosceles
	Sca Kind = "sca" // scalene
)

// KindFromSides determines whether given side lengths can form a triangle or not
func KindFromSides(a, b, c float64) Kind {
	// If any side is less then zero, automatically not a triangle
	if a <= 0 ||
		math.IsNaN(a) ||
		math.IsInf(a, 0) ||
		b <= 0 ||
		math.IsNaN(b) ||
		math.IsInf(b, 0) ||
		c <= 0 ||
		math.IsNaN(c) ||
		math.IsInf(c, 0) ||
		a+b < c ||
		b+c < a ||
		a+c<b {
		return NaT
	}

	// Check for equalateral triangle
	if a == b && a == c && b == c {
		return Equ
	}

	// Check for isosoles triangle
	if a == b || a == c || b == c {
		return Iso
	}

	return Sca
}
