    
pub fn main() -> i32 {
    sum_div_by(3) + sum_div_by(5) - sum_div_by(15)   
}

fn sum_div_by(num:i32) -> i32 {
    let target = 999;
    let p = target / num;
    num * ( p * (  p + 1 )) / 2
}

#[cfg(test)]
mod tests {
    
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(main(), 233168);
    }
}



