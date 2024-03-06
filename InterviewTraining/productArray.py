def arrayOfProducts(array):
    # Write your code here.
	retval=[]
    for i in range(len(array)):
		prod=1
		for j in range(len(array)):
			if j != i:
				prod *= array[j]
		retval.append(prod)
	return retval

