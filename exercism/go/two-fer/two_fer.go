// Prints 2-fer game
package twofer

import (
	"fmt"
)

// ShareWith should have a comment documenting it.
func ShareWith(name string) string {
	if name == "" {
		return "One for you, one for me.";
	} else {
		return fmt.Sprintf("One for %s, one for me.", name);
	}
}
