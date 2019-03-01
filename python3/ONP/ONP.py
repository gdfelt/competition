#!/bin/python3

def rev_polish_notation( expression ):
	# output
	output = []
	# stack
	stack = []

	for c in expression:
		if c.isalpha():
			output.append(c)

		#check if character is operator
		if c in "+-*/^":
			while (stack[len(stack) - 1] in "+-*/^") and (stack[len(stack) - 1] != '('):
				output.append(stack.pop())				
			stack.append(c)

		#check if character is left paren
		if c == '(':
			stack.append(c)

		#check if char is right paren
		if c == ')':
			while stack[len(stack) - 1] != '(':
				output.append(stack.pop())
			stack.pop()

	while len(stack) > 0:
		output.append(stack.pop())

	return ''.join(output)

def main():
	reps = int(input())
	for i in range(reps):
		print(rev_polish_notation(input()))

if __name__ == "__main__":
	main()	