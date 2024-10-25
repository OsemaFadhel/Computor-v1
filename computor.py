import math
import re

def parse_equation(input):

	# regex for matching the equation with the form of a * X^b where a is a float and b is an integer between 0 and 3
	regex_term = r"([+-]?\d*\.?\d*)\s*\*\s*X\^([0-9])"

	# coefficients of the equation
	coefficients = {}

	# split the equation into terms
	terms = input.split('=')
	if len(terms) != 2:
		raise Exception("Invalid equation")

	# parse the left side of the equation
	for match in re.finditer(regex_term, terms[0]):
		# get the coefficient and the power of the term
		power = int(match.group(2)) # exaple: 2 * X^2 = 0 => 2 because 2 is the power
		coefficient = float(match.group(1))
		# add the coefficient to the corresponding power
		# match.group(1) is the coefficient of the term which is for example 2 in 2 * X^2 = 0
		if power in coefficients:
			coefficients[power] += coefficient
		else:
			coefficients[power] = coefficient

	# parse the right side of the equation
	for match in re.finditer(regex_term, terms[1]):
		power = int(match.group(2))
		coefficient = float(match.group(1))
		# add the coefficient to the corresponding power
		# match.group(1) is the coefficient of the term which is for example 2 in 2 * X^2 = 0
		if power in coefficients:
			coefficients[power] -= coefficient
		else:
			coefficients[power] = -coefficient

	return coefficients

## to take in consideration: if coefficient is 0 print it, if coefficient is 1 print it, if power is 0 print it
## There might be exceptions you will have to manage. In the equation 42∗X0 = 42∗X0, for instance, each real number is a solution

def solve_equation(coefficients):
	flag_power = False
	polynomial_degree = max(coefficients.keys())

	reduced_form = "Reduced form: "
	for power, coefficient in coefficients.items():
		if coefficient != 0:
			if (power > 2):
				flag_power = True
			reduced_form += f"{coefficient} * X^{power} + "
	reduced_form = reduced_form[:-3] + " = 0"
	print(reduced_form)

	print("Polynomial degree:", polynomial_degree)

	if flag_power:
		raise Exception("The polynomial degree is stricly greater than 2, I can't solve.")

	print("The solution is:\n")

	## solve

