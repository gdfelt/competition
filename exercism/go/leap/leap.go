// Package leap calculates leap years in the gregorian calendar
package leap

// IsLeapYear calculates whether a given year is a leap year or not
func IsLeapYear(year int) bool {
	return year%400 == 0 || year%4 == 0 && year%100 != 0
}
