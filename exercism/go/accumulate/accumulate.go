package accumulate

// Accumulate executes a given operation on a collection
func Accumulate(collect []string, operation func(string) string) []string {

	output := []string{}

	for i := range collect {
		output = append(output, operation(collect[i]))
	}
	return output
}
