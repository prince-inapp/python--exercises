notes = {2000:0,
            500:0,
            200:0,
            100:0,
            50:0,
            20:0,
            10:0,
            5:0,
            2:0,
            1:0}

def getIntInput(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except Exception as e:
            print("Enter a whole number...Try again")

amount = getIntInput("Enter Amount: ")
for note in notes.keys():
    if amount>0:
        notes[note] = amount//note
        amount = amount - notes[note] * note
    else:
        break
for note, number in notes.items():
    if number>0:
        print("{}:{}".format(note, number))