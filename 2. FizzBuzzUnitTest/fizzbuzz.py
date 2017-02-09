'''
Task
Make it testable.
'''

def FizzBuzz(i):
		if i%5 == 0 and i%3 == 0:
			return "fizzbuzz"
		elif i%5 == 0:
			return "buzz"
		elif i%3 ==0:
			return "fizz"
		else:
			return i
if __name__ == "__main__":
	for i in range(1, 101):
		print(FizzBuzz(i))
