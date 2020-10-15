package clock

import (
	"fmt"
)

// Clock structure
type Clock struct {
	currTime int
}

// New function gives Clock constructor
func New(hours int, minutes int) Clock {
	// Calculates current minutes with positive only values
	currTime := (hours*60 + minutes) % (24 * 60)
	if currTime < 0 {
		currTime += 24 * 60
		currTime %= 24 * 60
	}
	return Clock{currTime}
}

// Add function adds time to a given clock
func (c Clock) Add(minutes int) Clock {
	return New((c.currTime/60)%24, c.currTime%60+minutes)
}

// Subtract function removes time from a given clock
func (c Clock) Subtract(minutes int) Clock {
	return c.Add(-minutes)
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.currTime/60, c.currTime%60)
}
