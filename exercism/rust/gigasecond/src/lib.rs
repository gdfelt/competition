use chrono::{DateTime, Duration, Utc};

const GIGASEC_IN_SECS: i64 = 1000000000;

// Returns a Utc DateTime one billion seconds after start.
pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    start + Duration::seconds(GIGASEC_IN_SECS)
}
