use unicode_segmentation::UnicodeSegmentation;

pub fn reverse(input: &str) -> String {
    // unimplemented!("Write a function to reverse {}", input);
    // let word: &str = input;
    input.graphemes(true).rev().collect()

}
