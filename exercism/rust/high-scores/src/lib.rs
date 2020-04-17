#[derive(Debug)]
pub struct HighScores {
    scores: Vec<u32>,
}

impl HighScores {
    pub fn new(scores: &[u32]) -> Self {
        HighScores {
            scores: scores.to_vec(),
        }
    }

    pub fn scores(&self) -> &[u32] {
        &self.scores
    }

    pub fn latest(&self) -> Option<u32> {
        match self.scores.len() {
            0 => None,
            _ => Some(self.scores[self.scores.len() - 1]),
        }
    }

    pub fn personal_best(&self) -> Option<u32> {
        match self.scores.iter().max() {
            None => None,
            Some(max) => Some(*max),
        }
    }

    pub fn personal_top_three(&self) -> Vec<u32> {
        let mut tmp_scores: Vec<u32> = self.scores.to_owned();
        tmp_scores.sort();
        tmp_scores.reverse();

        match self.scores.len() {
            0..=2 => (&tmp_scores[..self.scores.len()]).to_vec(),
            _ => (&tmp_scores[..3]).to_vec(),
        }
    }
}
