import random
import numpy as np
print("hello world")
nums = [] 
mu = 100
sigma = 50
    
for i in range(100): 
    temp = random.gauss(mu, sigma)
    nums.append(temp) 

a_file = open("test.txt", "w")
np.savetxt(a_file, nums)
a_file.close()
