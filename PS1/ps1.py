# This Python file uses the following encoding: utf-8
import os, sys

# Problem Set 1
# Name: Josh Haines
# Collaborators: None
# Time Spent: ~7hrs

# 	3 Credit Card Debt Problems

#	Problem 1: Paying the minimum.  Calculate the credit card balance after 
#	one year if a person only pays the minimum monthly payment required by 
#  	the	credit card company each month.
#
#	Problem 2: Calculating the minimum payment you can make and still pay 
#	off the loan in a year.  Two loops will iterate through a year to see 
#	final balance, and if it isn't big enough increase the guessed payment 
# 	amount and re-run the inner loop until you pay off the loan.

#	Problem 3: Very similar to problem 2, except use a bisection search
#	for the guessPayment to speed up the program.


def minimumPayment(currentBalance, percent):
	"""Take in a current balance and minimum payment percent, then return the 
	minimum payment"""
	currentBalance = float(currentBalance) #convert argument to float
	percent = float(percent) #convert argument to float
	percent = percent / 100
	if percent >= 100:
		sys.exit("Please provide a minimum payment percentage value less" + \
		"than 100 (eg. 2.5, 13, etc.).")
	payment = currentBalance * percent
	return payment

def interestPaidPerMonth(annualPercent,currentBalance):
	"""Function that takes in the annual interest rate percentage and the
	current principle balance and calualates how much interest must be 
	paid in that month.  Returns that interest amount."""
	annualPercent = float(annualPercent) #convert argument to float
	currentBalance = float(currentBalance) #convert argument to float
	annualPercent = annualPercent / 100
	interestPaid = annualPercent / 12 * currentBalance
	return interestPaid

def newBalance(oldBalance, monthlyRate, guessPayment):
	"""Calculate the remaining balance at the end of 12 months"""
	newBalance = (oldBalance * (1 + monthlyRate)) - guessPayment
	return newBalance

def balanceAfterYear(creditCardBalance,monthlyRate,guessPayment):
	"""This will take in the balance, monthlyRate, and payment then calculate 
	how much balance will be left after a year paying on the loan."""
	remainingBalance = creditCardBalance
	#main problem loops.  outer loop iterates if the guess isn't big enough
	#inner loop iterates to find the balance after a year of trial payments
	monthsNeeded = 0
	while monthsNeeded < 12 and remainingBalance > 0:
		remainingBalance = newBalance(remainingBalance,monthlyRate,guessPayment)
		monthsNeeded += 1
	return remainingBalance, monthsNeeded

def problemThreeCalcs(annualPercent,creditCardBalance):
	"""This is the entire calculations for the third problem.  This is pulled
	into a function in order to use return to break a value out of multiple
	levels of loops."""
	monthlyRate = (annualPercent / 100) / 12.0
	paymentLowerBound = creditCardBalance / 12
	paymentUpperBound = (creditCardBalance * ((1 + monthlyRate) ** 12)) / 12
	#main problem loops.  outer loop iterates if the guess isn't big enough
	#inner loop iterates to find the balance after a year of trial payments
	n = 1 #n is just a counter
	while n <= 1000:
		midPoint = (paymentLowerBound + paymentUpperBound) / 2 #new midpoint
		endingBalance, monthsNeeded = balanceAfterYear(creditCardBalance,monthlyRate,midPoint)
		endingBalance = round(float(endingBalance),2)
		if endingBalance == 0:
			return endingBalance,midPoint, n, monthsNeeded
		n += 1
		if (endingBalance > 0 and paymentLowerBound > 0) or (endingBalance < 0 and paymentLowerBound < 0):  #adjust the interval
			paymentLowerBound = midPoint
		else:
			paymentUpperBound = midPoint

def problemOne():
	"""Call this function to kick off the problem 1 solution"""
	#get the account balance and validate
	print "Please enter the current account balance."
	currentBalance = raw_input(">> ")
	currentBalance = float(currentBalance)
	
	#get the annual interest rate
	print "Please enter the annual interest rate."
	annualPercent = raw_input(">> ")
	annualPercent = float(annualPercent)

	#get the min payment percent and validate
	print "Please enter the minimum payment percentage."
	minPercent = raw_input(">> ")
	minPercent = float(minPercent)

	#main problem loop
	remainingBalance = round(float(currentBalance),2)
	totalPaid = 0.0
	for i in range(1,13):
		minimumMonthlyPayment = \
		round(float(minimumPayment(remainingBalance,minPercent)),2)
		principlePaid = round(float(minimumMonthlyPayment - \
			interestPaidPerMonth(annualPercent,remainingBalance)),2)
		interestPaid = \
		round(float(interestPaidPerMonth(annualPercent,remainingBalance)),2)
		remainingBalance = round((remainingBalance - principlePaid),2)
		print remainingBalance
		print "Month: %d" % (i)
		print "Minimum Monthly Payment: $%.2f" % (minimumMonthlyPayment)
		print "Principle paid: $%.2f" % (principlePaid)
		print "Remaining Balance: $%.2f" % (remainingBalance)
		totalPaid = totalPaid + principlePaid + interestPaid
	print "RESULT"
	print "Total Amount Paid: $%.2f" % totalPaid
	print "Remaining Balance: $%.2f" % remainingBalance
	start() #recall the start function to start over

def problemTwo():
	"""Call this function to kick off the problem 2 solution"""
	#get the credit card balance
	print "Please enter the outstanding credit card balance."
	creditCardBalance = raw_input(">> ")
	creditCardBalance = float(creditCardBalance)

	#get the annual interest rate
	print "Please enter the annual interest rate."
	annualPercent = raw_input(">> ")
	annualPercent = float(annualPercent)

	print "RESULT"
	guessPayment = 0.00
	remainingBalance = creditCardBalance
	monthlyRate = (annualPercent / 100) / 12.0 
	#main problem loops.  outer loop iterates if the guess isn't big enough
	#inner loop iterates to find the balance after a year of trial payments
	while remainingBalance > 0:
	 	remainingBalance = creditCardBalance
	 	monthsNeeded = 0
	 	guessPayment = guessPayment + .01
		#remainingBalance = balanceAfterYear(creditCardBalance,annualPercent,guessPayment,monthsNeeded)
		while monthsNeeded < 12 and remainingBalance > 0:
			remainingBalance = newBalance(remainingBalance,monthlyRate,guessPayment)
			monthsNeeded += 1
	print "Monthly payment to pay off debt in 1 year: %d" % guessPayment
	print "Number of months needed: %d" % monthsNeeded
	print "Balance: %.2f" % remainingBalance
	start() #recall the start function to start over

def problemThree():
	"""Call this function to kick off the problem 3 solution"""
	#get the credit card balance
	print "Please enter the outstanding credit card balance."
	creditCardBalance = raw_input(">> ")
	creditCardBalance = float(creditCardBalance)

	#get the annual interest rate
	print "Please enter the annual interest rate."
	annualPercent = raw_input(">> ")
	annualPercent = float(annualPercent)

	print "RESULT"
	endingBalance, midPoint, iterations, monthsNeeded = problemThreeCalcs(annualPercent,creditCardBalance,)
	print "Monthly payment to pay off debt in 1 year: %.2f" % midPoint
	print "Number of months needed: %d" % monthsNeeded  ##fix this
	print "Balance: %.2f" % endingBalance
	print "It took %d iterations." % iterations
	start() #recall the start function to start over

def start():     
	"""Function to kick things off."""     
	print "Welcome to the credit card processing center."     
	print "If you would like to calculate your credit card balance after" + \
	" a year of only paying the minimum payment...please Press 1."
	print "If you would like to calculate your minimum payment to pay off" + \
	" your balance in 12 months...please Press 2."
	print "If you would like to calculate your minimum payment to pay off" + \
	" your balance in 12 months...please Press 3. (Bisection serach solution)"
	print "If you would like to exit...please press 4"
	choice = raw_input(">> ")
	choice = int(choice)
	if isinstance( choice, int ):
		if choice == 1:
			problemOne()
		elif choice == 2:
			problemTwo()
		elif choice == 3:
			problemThree()
		elif choice == 4:
			sys.exit("exiting...")
	else:
		sys.exit("You are dumb, exiting...")

start();
#end