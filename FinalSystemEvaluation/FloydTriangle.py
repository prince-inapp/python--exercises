def getIntInput(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except Exception as e:
            print("Enter a whole number...Try again")

row = getIntInput("Enter Number of Rows : ")
num = 1
for i in range(0,row+1):
    for j in range(0,i):
        print(num, end = "\t")
        num = num+1
    print()
