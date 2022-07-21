import random
import time

rules = {'rock':'scissors', 
        'paper':'rock', 
        'scissors':'paper'}

items = {1:'rock',2:'scissors',3:'paper'}
count = 0
computer_point = 0
user_point = 0
print("Welcome to Rock...Paper...Scissors")
while(count<5):    
    print('''
        Choose an option :
        1. Rock
        2. Paper
        3. Scissors
        ''')
    option = int(input('::__'))
    if option not in items.keys():
        print("invalid option")
    else:
        user_option = items[option]
        computer_option = items[random.randint(1,3)]
        if(rules[computer_option]== user_option):
            computer_point+=1
            time.sleep(1)
            print("Computer chooses {}. \n computer wins this round! \n  Computer Score - {} \n User Score - {}".format(computer_option, computer_point, user_point))
            count+=1
        elif(rules[user_option] == computer_option):
            user_point += 1
            count+=1
            time.sleep(1)
            print("Computer chooses {}. \n user wins this round!\n Computer Score - {} \n User Score - {}".format(computer_option, computer_point, user_point))
        else:
            print("Computer chooses {}. Round Tied!".format(computer_option))
print('--------------------------------------------')
time.sleep(1)
if(computer_point>user_point):
    print("Computer Wins the Game!!!\n Computer Score - {} \n User Score - {}".format(computer_point,user_point))
elif(user_point>computer_point):
    print("User Wins the Game!!!\n Computer Score - {} \n User Score - {}".format(computer_point,user_point))
else:
    print("Game Tied")
print('---------------------------------------------')