"""Do some stuff with polynomials.

Going to try and write up a nice docstring to get rid of the error.
We'll see.
"""

import sys
# 6.00 Problem Set 2
#
# Successive Approximation


def call_poly():
    """Get poly inputs and send them to compute_deriv function."""
    print("Enter your polynomial coefficient list.  (Format: 0 3 51 ...)")
    poly_input = input(">>")
    poly = [float(x) for x in poly_input.split()]
    print(poly)
    print("Enter your x value.")
    x = float(input(">>"))
    print(evaluate_poly(poly, x))
    start()


def call_deriv():
    """Get poly inputs and send them to compute_deriv function."""
    print("Enter your polynomial coefficient list.  (Format: 0 3 51 ...)")
    poly_input = input(">>")
    poly = [float(x) for x in poly_input.split()]
    print(compute_deriv(poly))
    start()


def call_compute_root():
    """Call a the computeRoot function.

    Get poly input, initial guess, and epsilon (error amount) and send,
    them all to compute_root function.
    """
    print("Enter your polynomial coefficient list.  (Format: 0 3 51 ...)")
    poly_input = input(">>")
    poly = [float(x) for x in poly_input.split()]
    print(poly)
    print("Enter your initial guess at a root for the previous polynomial.")
    guess = input(">>")
    print("Enter an epsilon or error amount value.")
    epsilon = input(">>")
    print(compute_root(poly, guess, epsilon))
    start()


def evaluate_poly(poly, x):
    """Compute the polynomial function for a given value x.

    Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> printevaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 +
    5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # polyLength = len(poly)
    # print"You've entered a value which corresponds to the polynomial:"
    # for i in range(len(poly)):
    #     print%fx^%d" % (poly[i],i)
    x = float(x)
    # print"Your x value was %f" % x
    # print"Starting Calcs"
    total = 0.0
    for i in range(len(poly)):
        total += (x ** i) * poly[i]
    return total


def compute_deriv(poly):
    """Compute and returns the derivative of a polynomial function.

    If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> printcompute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # print"You've entered a value which corresponds to the polynomial:"
    # for i in range(len(poly)):
    #     print%fx^%d" % (poly[i],i)
    # print"Starting Calcs"
    poly2 = list(poly)
    derivative = poly2
    # printderivative
    for i in range(len(poly2)):
        derivative[i] = derivative[i] * (i)
    derivative = derivative[1:len(derivative)]
    return derivative


def compute_root(poly, guess, epsilon):
    """Function computes the root of a function.

    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> guess = 0.1
    >>> epsilon = .0001
    >>> printcompute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    guess: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # See if guess is close enough right away
    deriv = compute_deriv(poly)

    guess = float(guess)
    epsilon = float(epsilon)
    total = abs(evaluate_poly(poly, guess))
    answer = [0.0, 0]
    if total < epsilon:
        print("We've found a root!")
        answer[0] = guess
        answer[1] = 1
        return answer
    else:
        print("Inital Guess is Incorrect...Calculating")

    new_guess = guess
    num_guesses = 1      # define counter

    # iterate our new guess until it gets smaller than epsilon
    while abs(evaluate_poly(poly, new_guess)) > epsilon:
        new_guess = new_guess - (evaluate_poly(poly, new_guess)) / \
            (evaluate_poly(deriv, new_guess))
        print("%f as a guess yields %f." % (new_guess, evaluate_poly(poly,
              new_guess)))
        num_guesses += 1
        if num_guesses > 100:     # don't let the while loop go forever
            return "failed..."
    answer[0] = new_guess
    answer[1] = num_guesses
    return answer


def start():
    """Call one of the three functions in this worksheet.

    Get a user input and call the correct function.  Re-call this
    function after each of the choices runs.
    *Includes an exit value.
    """
    print("Enter 1 to call the polynomial function")
    print("Enter 2 to call the derivative function")
    print("Enter 3 to call the root function")
    print("Enter 4 to exit")
    choice = input(">>")
    if choice == "1":
        call_poly()

    elif choice == "2":
        call_deriv()
    elif choice == "3":
        call_compute_root()
    else:
        sys.exit("exiting...")

start()
# end
