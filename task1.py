#print 10 lines, each printing 'hello &N', where N is thw line number

#for i in range(1,11):
#	result = 'hello ' + str(i)
#	print (result)

#for i in range(10)

# for type chect => type(1); type (3.0)...'
#
def add_number_to_hello(i): #if (i) change to (i=1) every number will be 1
	"""
	Function documentaion goes here
	
	"""
	result = 'hello {0}'.format(i)
	return result

for i in range(1,11):
	print(add_number_to_hello(i))
