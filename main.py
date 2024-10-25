from computor import parse_equation, solve_equation
import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <equation>")
	else:
		try:
			coefficients = parse_equation(sys.argv[1])
			if coefficients is None:
				raise Exception("Invalid equation")
			solve_equation(coefficients)
		except Exception as e:
			print(e)
