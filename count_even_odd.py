nums = [1,2548,4,3,58,45,74,21,36,22,230,78,13,35,25,93,81]
countOdd = 0
countEven = 0
for i in nums:
    if(i%2==0):
        countEven+=1
    else:
        countOdd+=1
print("List is ", nums)
print("number of odd numbers are {}".format(countOdd))
print("number of even numbers are {}".format(countEven))
