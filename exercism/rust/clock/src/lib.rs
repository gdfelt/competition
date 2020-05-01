use std::fmt;

#[derive(Copy, Clone, Debug)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let curr_time: i32 = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

        Clock {
            hours: (curr_time / 60) % 24,
            minutes: curr_time % 60,
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        let tmp_clock: Clock = *self;
        Clock::new(tmp_clock.hours, tmp_clock.minutes + minutes)
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
