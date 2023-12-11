package Advent2023

import (
	"testing"
)

func TestDay01p1(t *testing.T){
	target := 54450
	res, err := Day01p1()
	if err != nil {
		t.Fatalf("Day 01 part 1: error occured: %s", err)
	}
	if res != target {
		t.Fatalf("Day 01 part 1: wanted %d but got %d", target, res)
	}
}

func TestDay01p2(t *testing.T){
	target := 54450
	res, err := Day01p2()
	if err != nil {
		t.Fatalf("Day 01 part 2: error occured: %s", err)
	}
	if res != target {
		t.Fatalf("Day 01 part 2: wanted %d but got %d", target, res)
	}
}