/// "Encipher" with the Atbash cipher.
pub fn encode(plain: &str) -> String {
    plain
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| match c {
            c if c.is_uppercase() => std::char::from_u32(187 - (c as u32)).unwrap(),
            c if c.is_lowercase() => std::char::from_u32(219 - (c as u32)).unwrap(),
            _ => c,
        })
        .enumerate()
        .fold(String::new(), |acc, (i, c)| {
            if i != 0 && i % 5 == 0 {
                format!("{} {}", acc, c)
            } else {
                format!("{}{}", acc, c)
            }
        })
}

/// "Decipher" with the Atbash cipher.
pub fn decode(cipher: &str) -> String {
    cipher
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| match c {
            c if c.is_uppercase() => std::char::from_u32(155 - (c as u32)).unwrap(),
            c if c.is_lowercase() => std::char::from_u32(219 - (c as u32)).unwrap(),
            _ => c,
        })
        .collect()
}
