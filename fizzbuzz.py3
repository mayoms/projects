'''
Created on Dec 13, 2014

@author: mayoms

This is part of a CodeEval challenge as described:

Your program should accept a file as its first argument. The file contains multiple separated lines; 
each line contains 3 numbers that are space delimited. The first number is the first divider (X), the 
second number is the second divider (Y), and the third number is how far you should count (N). You may 
assume that the input file is formatted correctly and the numbers are valid positive integers.

Print out the series 1 through N replacing numbers divisible by X with “F”, numbers divisible by Y with “B” 
and numbers divisible by both with “FB”. Since the input file contains multiple sets of values, your output 
should print out one line per set. Ensure that there are no trailing empty spaces in each line you print.

This description is from the CodeEval website.

'''
if __name__ == '__main__':
    pass

def FizzBuzz(f,b,n):
	if n % f == 0 and n % b == 0:
		return "FB"
	if n % f == 0:
		return "F"
	if n % b == 0:
		return "B"
	return str(n)

with open("fizzbuzz.txt","r") as readfile:
	for line in readfile.readlines():
		line.strip("\n")
		line = [int(i) for i in line]
		print(" ".join([FizzBuzz(line[0],line[1],n) for n in range(1,line[2]+1)]))

