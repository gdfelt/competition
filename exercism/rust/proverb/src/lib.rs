pub fn build_proverb(list: &[&str]) -> String {
    const ENDING: &str = "And all for the want of a ";

    let mut proverb: String = String::from("");

    if list.len() > 0 {
        for s in 0..list.len() - 1 {
            proverb = proverb + "For want of a " + list[s] + " the " + list[s + 1] + " was lost.\n";
        }

        proverb = proverb + &ENDING + list[0] + ".";
    }

    proverb
}
