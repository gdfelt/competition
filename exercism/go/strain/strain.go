package strain

import (
// "fmt"
)

type Ints []int
type Lists [][]int
type Strings []string

// Keep takes list of ints and filters based on function
func (ints *Ints) Keep(f func(int) bool) Ints {

	ret := []int{}
	for _, num := range *ints {
		if f(num) {
			ret = append(ret, num)
		}
	}

	if len(ret) == 0 {
		return Ints(nil)
	}

	return Ints(ret)
}

// Discard takes list of ints and filters based on function
func (ints *Ints) Discard(f func(int) bool) Ints {
	ret := []int{}
	for _, num := range *ints {
		if !f(num) {
			ret = append(ret, num)
		}
	}

	if len(ret) == 0 {
		return Ints(nil)
	}

	return Ints(ret)
}

// Keep takes list of lists and filters based on function
func (lists *Lists) Keep(f func([]int) bool) Lists {
	ret := [][]int{}
	for _, l := range *lists {
		if f(l) {
			ret = append(ret, l)
		}
	}

	if len(ret) == 0 {
		return Lists(nil)
	}

	return Lists(ret)
}

// Discard takes list of lists and filters based on function
func (lists *Lists) Discard(f func([]int) bool) Lists {
	return Lists(nil)
}

// Keep takes list of strings and filters based on function
func (strings *Strings) Keep(f func(string) bool) Strings {
	ret := []string{}
	for _, s := range *strings {
		if f(s) {
			ret = append(ret, s)
		}
	}

	if len(ret) == 0 {
		return Strings(nil)
	}

	return Strings(ret)
}

// Discard takes list of strings and filters based on function
func (strings *Strings) Discard(f func(string) bool) Strings {
	return Strings(nil)
}
