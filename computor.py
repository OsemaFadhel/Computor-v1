import math
import re

def parse_equation(input):

	# regex for matching the equation with the form of a * X^b where a is a float and b is an integer between 0 and 3
	regex_term = r"([+-]?\d*\.?\d*)\s*\*\s*X\^([0-2])"

	# coefficients of the equation
	coefficients = {0: 0, 1: 0, 2: 0}

	# split the equation into terms
	terms = input.split('=')
	if len(terms) != 2:
		raise Exception("Invalid equation")

	# parse the left side of the equation
	for match in re.finditer(regex_term, terms[0]):
		# get the coefficient and the power of the term
		power = int(match.group(2)) # exaple: 2 * X^2 = 0 => 2 because 2 is the power
		# add the coefficient to the corresponding power
		# match.group(1) is the coefficient of the term which is for example 2 in 2 * X^2 = 0
		coefficients[power] += float(match.group(1)) # exaple: 2 * X^2 = 0 => 2 + 0 = 2

	# parse the right side of the equation
	for match in re.finditer(regex_term, terms[1]):
		power = int(match.group(2))
		coefficients[power] -= float(match.group(1)) # exaple: 2 * X^2 = 0 => 2 - 0 = 2

	return coefficients

def solve_equation(coefficients):
	reduced_form = "Reduced form: "
	for power, coefficient in coefficients.items():
		if coefficient != 0:
			reduced_form += f"{coefficient} * X^{power} + "
	reduced_form = reduced_form[:-3] + " = 0"
	print(reduced_form)
