public class Hamming {

    private String leftStrand;
    private String rightStrand;

    public Hamming(String leftStrand, String rightStrand) {

        if (leftStrand == "") { throw new IllegalArgumentException("left strand must not be empty."); }
        if (rightStrand == "") { throw new IllegalArgumentException("right strand must not be empty."); }

        if(leftStrand.length() != rightStrand.length()){
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }

        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
    }

    public int getHammingDistance() {
//        throw new UnsupportedOperationException("Delete this statement and write your own implementation.");
//        return (self.leftStrand ^ self.rightStrand).length();
        int diff_count = 0;
        int index = 0;

        for( char c : leftStrand.toCharArray()) {
            if(c != rightStrand.charAt(index)){
                diff_count++;
            }
            index++;
        }
        
        // return 0;
        return diff_count;

    }
}
