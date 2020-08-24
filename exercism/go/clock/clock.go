package clock

import (
	"fmt"
)

// Clock structure
type Clock struct {
	hours   int
	minutes int
}

// New function gives Clock constructor
func New(hours int, minutes int) Clock {
	// Calculates current minutes with positive only values
	currTime := ((hours*60+minutes)%1440 + 1440) % 1440
	return Clock{(currTime / 60) % 24, currTime % 60}
}

// Add function adds time to a given clock
func (c Clock) Add(minutes int) Clock {
	return New(c.hours, c.minutes+minutes)
}

// Subtract function removes time from a given clock
func (c Clock) Subtract(minutes int) Clock {
	return c.Add(-minutes)
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.hours, c.minutes)
}
