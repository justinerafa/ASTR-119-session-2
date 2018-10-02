import numpy as np  #we use numpy alot 

def main():
	i = 0  #declare i = 0
	n = 10  #declare n = 10
	x = 119.0  #float x, these have a . 
	
	#we can use numpy to quickly make arrays 
	y = np.zeros(n, dtype=float) #declares 10 zeros 
	
	#we can use for loops to iterate through a variable 
	
	for i in range(n):  #i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 #set y = 2i+1 as floats 
		
	for y_element in y:
		print(y_element)
		
if __name__ == "__main__":
	main()