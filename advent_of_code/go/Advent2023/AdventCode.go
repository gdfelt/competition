package Advent2023

import (
	"bufio"
	"errors"
	"os"
)

func Day01p1() (int, error) {

	file, err := os.Open("./data/Day1p1.dat")
	if err != nil {
		return -1, errors.New("Unable to open data file")
	}
	
	scan := bufio.NewScanner(file)
	scan.Split(bufio.ScanLines)
	sum := 0
	var lines []string
	for scan.Scan(){
		lines = append(lines, scan.Text())
	}
	file.Close()

	for _, line := range lines {
		firstNum, secondNum := 0, 0
 		for _, elem := range line {
			if elem >= 48 && elem <= 57 {
				firstNum = int(elem) - 48
				break
			}
		} 

		for i := len(line) - 1; i >= 0; i-- {
			c := byte(line[i])
			if c >= 48 && c <= 57 {
				secondNum = int(c) - 48
				break
			} 
		}
		sum += firstNum * 10 + secondNum
	}

	return sum, nil
}

func Day01p2() (int, error) {


	return 123, nil
}