# print all the numbers which are div by 5 and multiple of 8 between 2000 and 2500

nums = []
for i in range(2000,2501,1):
    if((i%5==0) and(i%8==0)):
        nums.append(i)
print(nums)

#multiplication table

number = int(input("Enter number :"))
for i in range(1,11,1):
    print("{} x {} = {}".format(i,number,i*number))