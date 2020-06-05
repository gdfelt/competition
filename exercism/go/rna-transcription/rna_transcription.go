package strand

// ToRNA is a function that produces the compliment of a dna strand
func ToRNA(dna string) string {

	compliment := ""

	for _, c := range dna {
		switch c {
		case 'A':
			compliment += "U"
		case 'C':
			compliment += "G"
		case 'G':
			compliment += "C"
		case 'T':
			compliment += "A"
		default:

		}
	}

	return compliment
}
