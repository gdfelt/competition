package phonenumber

import (
	"errors"
	"fmt"
	"unicode"
)

func parsePhone(input string) (string, error) {

	s := ""

	for _, r := range input {
		if unicode.IsNumber(r) {
			s = s + string(r)
		}
	}

	if len(s) != 10 {
		if len(s) == 11 && s[0] == '1' {
			s = s[1:]
		} else {
			return "", errors.New("Country Code must be One")
		}
	}

	if s[0] == '0' || s[0] == '1' {
		return "", errors.New("Area code cannot start with Zero or One")
	}

	if s[3] == '0' || s[3] == '1' {
		return "", errors.New("Exchange code cannot start with Zero or One")
	}

	return s, nil
}

func Number(input string) (string, error) {
	number, err := parsePhone(input)
	if err != nil {
		return "", err
	}
	return number, nil
}

func AreaCode(input string) (string, error) {
	number, err := parsePhone(input)
	if err != nil {
		return "", err
	}
	return number[:3], nil
}

func Format(input string) (string, error) {
	number, err := parsePhone(input)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("(%s) %s-%s", number[:3], number[3:6], number[6:]), nil
}
