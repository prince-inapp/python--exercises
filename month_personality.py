def dob_fun(mon):
    match mon:
        case 1 : return  "People born in January are bold and alert.\nBirth Stone : Garnet"
        case 2 : return "People born in February are lucky and loyal.\nBirth Stone : Amethyst"
        case 3 : return "People born in March are naughty and genius.\nBirth Stone : Aquamarine"
        case 4 : return "People born in April are caring and strong.\nBirth Stone : Diamond"
        case 5 : return "People born in may are loving and practical.\nBirth Stone : Emerald"
        case 6 : return "People born in June are romantic and curious,\nBirth Stone : Alexandrite"
        case 7 : return "People born in July are adventerous and honest.\nBirth Stone : Ruby"
        case 8 : return "People born in July are adventerous and honest.\nBirth Stone : Ruby"
        case 9 : return "People born in September are sensitive and pretty.\nBirth Stone : Sapphire"
        case 10 : return "People born in October are Stylish and friendly.\nBirth Stone : Tourmaline"
        case 11 : return "People born in November are nice and creative.\nBirth Stone : Citrine"
        case 12 : return "People born in december are confident and freedom loving.\nBirth Stone : Zircon"

dob = int(input("enter your dob month number :"))
if dob == 1:
    print("People born in January are bold and alert")
    print("Birth Stone : Garnet")
elif(dob==2):
    print("People born in February are lucky and loyal")
    print("Birth Stone : Amethyst")
elif(dob==3):
    print("People born in March are naughty and genius")
    print("Birth Stone : Aquamarine")
elif(dob==4):
    print("People born in April are caring and strong")
    print("Birth Stone : Diamond")
elif(dob==5):
    print("People born in may are loving and practical")
    print("Birth Stone : Emerald")
elif(dob==6):
    print("People born in June are romantic and curious")
    print("Birth Stone : Alexandrite")
elif(dob==7):
    print("People born in July are adventerous and honest")
    print("Birth Stone : Ruby")
elif(dob==8):
    print("People born in August are active and hardworking")
    print("Birth Stone : Peridot")
elif(dob==9):
    print("People born in September are sensitive and pretty")
    print("Birth Stone : Sapphire")
elif(dob==10):
    print("People born in October are Stylish and friendly")
    print("Birth Stone : Tourmaline")
elif(dob==11):
    print("People born in November are nice and creative")
    print("Birth Stone : Citrine")
elif(dob==12):
    print("People born in december are confident and freedom loving")
    print("Birth Stone : Zircon")
else:
    print("Invalid Month")
print("\n")
print(dob_fun(dob))