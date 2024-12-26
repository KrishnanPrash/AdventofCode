import numpy as np
from collections import defaultdict

#############  Part 1 ############# 
f = open("day1_input.txt", "r")

data = [x.split() for x in f.readlines()]
list1, list2 = np.array([int(x[0]) for x in data]), np.array([int(x[1]) for x in data])

list1.sort()
list2.sort()

distances = list1 - list2

totalDistance = sum([abs(x) for x in distances])
print(f"The total distance is {totalDistance}")

#############  Part 2 ############# 
weights = defaultdict(int)
for x in list2:
    weights[x] += 1

similarity_score = sum([num*weights[num] for num in list1])

print(f"The similarity score is {similarity_score}")
f.close()

