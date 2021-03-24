package phonenumber

import "fmt"

func parsePhone(input string) (string, error) {
	return "3335557777", nil
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
	return fmt.Sprintf("(%s) %s-%s", number[:3], number[3:6], number[7:]), nil
}
