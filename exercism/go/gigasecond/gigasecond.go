// Package gigasecond calculates a Gigasecond from a given time
package gigasecond

import "time"

// AddGigasecond calculates a Gigasecond from a given time
func AddGigasecond(t time.Time) time.Time {
	return t.Add(time.Second * 1000000000)
}
