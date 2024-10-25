# Computor v1

This project aims to make you code a simple equation solving program. It will take polynomial equations into account. These equations will only require exponents. No complex
function. The program will have to display its solution(s).

## Description of the project

Program that solves a polynomial second or lower degree equation. It will to show at least: </br>
 - The equation in its reduced form.
 - The degree of the equation.
 - It’s solution(s) and the polarity of the discriminant if it makes sens.

Examples:

```bash
$><span style="color:green;">./computor</span> "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
<span style="color:blue;">Reduced form:</span> 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
<span style="color:blue;">Polynomial degree:</span> 2
<span style="color:blue;">Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
$><span style="color:green;">./computor</span> "5 * X^0 + 4 * X^1 = 4 * X^0"
<span style="color:blue;">Reduced form:</span> 1 * X^0 + 4 * X^1 = 0
<span style="color:blue;">Polynomial degree:</span> 1
<span style="color:blue;">The solution is:</span>
-0.25
$><span style="color:green;">./computor</span> "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
<span style="color:blue;">Reduced form:</span> 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
<span style="color:blue;">Polynomial degree:</span> 3
<span style="color:red;"> The polynomial degree is strictly greater than 2, I can't solve.</span>
```

We will always expect the entry to have the right format, ie. every term respect the
form a ∗ x^p. Exponents are organized and present. It doesn’t mean the equation
has a solution! If so, your program should detect it and specify it. You should also think
of zero, negative or non whole coefficients...
