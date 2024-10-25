import math
import re

def parse_equation(input):

	# regex for matching the equation with the form of a * X^b where a is a float and b is an integer between 0 and 3
	regex_term = r"([+-]?\s*\d*\.?\d*)\s*\*\s*X\^([0-9])"

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
		coefficient = float(match.group(1).replace(" ", ""))
		# add the coefficient to the corresponding power
		# match.group(1) is the coefficient of the term which is for example 2 in 2 * X^2 = 0
		if power in coefficients:
			coefficients[power] += coefficient
		else:
			coefficients[power] = coefficient

	# parse the right side of the equation
	for match in re.finditer(regex_term, terms[1]):
		power = int(match.group(2))
		coefficient = float(match.group(1).replace(" ", ""))
		# add the coefficient to the corresponding power
		# match.group(1) is the coefficient of the term which is for example 2 in 2 * X^2 = 0
		if power in coefficients:
			coefficients[power] -= coefficient
		else:
			coefficients[power] = -coefficient

	# order the coefficients by power
	coefficients = dict(sorted(coefficients.items(), key=lambda x: x[0]))

	return coefficients

## to take in consideration: if coefficient is 0 print it, if coefficient is 1 print it, if power is 0 print it
## There might be exceptions you will have to manage. In the equation 42∗X0 = 42∗X0, for instance, each real number is a solution

def solve_equation(coefficients):
	flag_power = False
	polynomial_degree = max(coefficients.keys())

	reduced_form = "Reduced form: "
	first_iteration = True
	for power, coefficient in coefficients.items():
		if power > 2:
			flag_power = True
		# if coefficient is positive, we add a + sign before it. but not for the first term
		if first_iteration:
			if coefficient < 0:
				reduced_form += f"- {-coefficient} * X^{power} "
			else:
				reduced_form += f"{coefficient} * X^{power} "
			first_iteration = False
		else:
			if coefficient < 0:
				reduced_form += f"- {-coefficient} * X^{power} "
			else:
				reduced_form += f"+ {coefficient} * X^{power} "

	reduced_form = reduced_form[:-1] + " = 0"
	print(reduced_form)

	print("Polynomial degree:", polynomial_degree)

	if flag_power:
		raise Exception("The polynomial degree is stricly greater than 2, I can't solve.")

	## solve
	if polynomial_degree == 0:
		if coefficients[0] == 0:
			print("All real numbers are solutions")
		else:
			print("No solution")
	elif polynomial_degree == 1: # if polynomial degree is 1, we have one real solution
		print("The solution is:\n", -coefficients[0] / coefficients[1])
	elif polynomial_degree == 2:
		discriminant = pow(coefficients[1], 2) - (4 * coefficients[2] * coefficients[0])  # b^2 - 4ac
		if discriminant > 0: # if discriminant is positive, we have two real solutions -b ± √Δ / 2a
			print("Discriminant is strictly positive, the two solutions are:")
			print((-coefficients[1] - math.sqrt(discriminant)) / (2 * coefficients[2]))
			print((-coefficients[1] + math.sqrt(discriminant)) / (2 * coefficients[2]))
		elif discriminant == 0: # if discriminant is 0, we have one real solution -b / 2a
			print("The solution is:\n", -coefficients[1] / (2 * coefficients[0]))
		else: # if discriminant is negative, we have two complex solutions (-b ± i√-Δ) / 2a, where i is the imaginary unit defined by i = √-1
			print("Discriminant is strictly negative, the two solutions are:")
			print(f"({-coefficients[1]} - i√{-discriminant}) / {2 * coefficients[2]}")
			print(f"({-coefficients[1]} + i√{-discriminant}) / {2 * coefficients[2]}")
