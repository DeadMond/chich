def positive_sum(arr):

positiveSum = 0

for i in arr:
if i >= 0:
positiveSum += i
return positiveSum

print(positive_sum([1, 2, -3, 7]))
