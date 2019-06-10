pub mod euler001 {
    
    pub fn main() -> i32 {
        3 
    }

    #[cfg(test)]
    mod tests {
        
        use super::*;

        #[test]
        fn test_add() {
            assert_eq!(main(), 3);
        }
    }

}


