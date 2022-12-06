class MyVector:
	pass
	## put your class definition here.


if __name__ == '__main__':

	#####################################
	## Builtins
	#####################################
	x0 = MyVector()
	# print() prints all the elements as below in comment
	print (x0)		# MyVector()

	# passing illegal type to constructor
	#xx = MyVector(33, 'str2') # raises 'ValueError' exception


	x1 = MyVector(3,5,99,0)
	# len() returns number of elements
	print (len(x1))	# 4
	# print() prints all the elements as below in comment
	print (x1)		# MyVector(3,5,99,0)

	# MyVector should can be used as an iterable in loops
	for elem in x1:
		print(elem)	# prints 3 5 99 0 on separte lines

	print(x1[2])	# 99
	#print(x1[5])	# raises 'IndexError' exception
	x1[2] = 33
	print(x1)		# MyVector(3,5,33,0)

	# abs() should return absolute value: sqrt(sum(square_of_each_elemnent))
	x2 = MyVector(3,4)
	print(abs(x2))	# 5.0


	# MyVector should be false if empty or abs()>0, otherwise true 
	if x1:	# True
		print("this line will print")
	if x0:	# True
		print("this line will NOT print")

	#####################################
	## Arithmetic
	#####################################
	x1 = MyVector(1,2,3)
	x2 = MyVector(4,5,6)
	# + should add corresponding elements and return result
	x3 = x1+x2
	print(x1)	# MyVector(1,2,3)	
	print(x2)	# MyVector(4,5,6)	
	print(x3)	# MyVector(5,7,9)

	x1 += x2
	print(x1)	# MyVector(5,7,9)
	print(x2)	# MyVector(4,5,6)	

	# * should multiply constant with each element
	x1 = MyVector(1,2,3)
	x2 = x1*3
	x3 = 3*x1
	print(x1)	# MyVector(1,2,3)	
	print(x2)	# MyVector(3,6,9)	
	print(x3)	# MyVector(3,6,9)


	# << should rotate elements
	x1 = MyVector(1,2,3)
	x2 = x1<<1
	print(x2) 	# MyVector(2,3,1)

