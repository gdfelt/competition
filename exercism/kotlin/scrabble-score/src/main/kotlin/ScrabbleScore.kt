object ScrabbleScore {

    fun scoreLetter(c: Char): Int {
        return when(c.toLowerCase()){
            'a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't' -> 1
            'd', 'g' -> 2
            'b', 'c', 'm', 'p' -> 3
            'f', 'h', 'v', 'w', 'y' -> 4
            'k' -> 5
            'j', 'x' -> 8
            'q', 'z' -> 10
            else -> -1

        }

        //TODO("Implement this function to complete the task")
    }

    fun scoreWord(word: String): Int {
        
        var score: Int = 0
        for (c in word){
            score += scoreLetter(c)
        }
        
        return score
        //TODO("Implement this function to complete the task")
    }
}
