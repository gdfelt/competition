use std::fmt;

#[derive(Copy, Clone, Debug)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let clock: Clock = Clock {
            hours: 0,
            minutes: 0,
        }
        .add_minutes(hours * 60 + minutes);
        clock
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        let mut clock: Clock = *self;
        // Convert time to number of minutes and add minute modifications
        let mut curr_time: i32 = (clock.hours * 60 + clock.minutes) + (minutes % 1440);

        // Wrap around if negative
        if curr_time < 0 {
            curr_time = curr_time + 1440
        }

        // Convert back to hrs, mins
        clock.hours = (curr_time / 60) % 24;
        clock.minutes = curr_time % 60;

        clock
    }
}

impl PartialEq for Clock {
    fn eq(&self, other: &Self) -> bool {
        self.hours == other.hours && self.minutes == other.minutes
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}
