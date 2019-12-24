

pub fn main() -> i32 {
    let limit = 4000000;
    let mut a = 2;
    let mut b = 8;
    let mut tmp;
    let mut sum = a + b;

    loop {
        tmp = 4 * b + a;
        if tmp > limit {
            break;
        }
        a = b;
        b = tmp;
        sum = sum + b;

    }
    sum

}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_even_fib() {
        assert_eq!(main(), 4613732)
    }
}

