import random

diff = "easy"
score = 0
blocks = []

def GenerateEasy():
    for i in range(15):
        num = random.randint(1, 10)
        blocks.append(num)
    return blocks

def GenerateMedium():
    for i in range(15):
        num = random.randint(1, 50)
        blocks.append(num)
    return blocks
        
def GenerateHard():
    for i in range(15):
        num = random.randint(1, 100)
        blocks.append(num)
    return blocks

def menu(diff):
    print(" 1. Play", '\n', "2. Difficulty", '\n', "3. Quit", '\n')
    user = int(input("Please select a difficulty and then press play ! "))
    if user == 1:
        print("Which mode would you like to play ?", '\n',"1. Addition", '\n', "2. Subtraction", '\n', "3. Multiplication", '\n')
        mode = int(input())
        if mode == 1:
            game(blocks, score, diff)
        if mode == 2:
            GenerateMedium()
            subtraction(blocks, score, diff)
        if mode == 3:
            multiplication(blocks, score, diff)
    elif user == 2:
        print("Difficulty determines the highest value in which numbers used may have", '\n', "Easy", '\n', "Medium", '\n', "Hard")
        diff = input("Please choose a difficulty ").lower()
        if diff == "easy":
            print("Easy selected ! Generating Numbers...", '\n')
            GenerateEasy()
            menu(diff)
        if diff == "medium":
            print("Medium selected ! Generating Numbers...", '\n')
            GenerateMedium()
            menu(diff)
        if diff == "hard":
            print("Hard selected ! Generating Numbers...", '\n')
            GenerateHard()
            menu(diff)
        else:
            print("ERROR: Unrecognised input, please try again")
            menu(diff)
    elif user == 3:
        quit()
    else:
        print("ERROR: Unrecognised input, please try again")
        menu(diff)

def game(blocks, score, diff):
    move = False
    while move != True:
        print("Your starting numbers are", blocks)
        valuone = random.randint(1, 15)
        valutwo = random.randint(1, 15)
        answer = blocks[valuone] + blocks[valutwo]
        print("? + ? =", answer)
        useone = int(input("Please enter your first value: "))
        usetwo = int(input("Please enter your second value: "))
        
        if useone and usetwo in blocks:
            if useone + usetwo == answer:
                score += 10
                blocks.remove(useone)
                blocks.remove(usetwo)
                print("That's correct !", '\n', "Your current score is:", score)
                move = True
                if diff == "easy":
                    newo = random.randint(1, 10)
                    newt = random.randint(1, 10)
                    blocks.append(newo)
                    blocks.append(newt)
                    game(blocks, score, diff)
                if diff == "medium":
                    newo = random.randint(1, 50)
                    newt = random.randint(1, 50)
                    blocks.append(newo)
                    blocks.append(newt)
                    game(blocks, score, diff)
                else:
                    newo = random.randint(1, 100)
                    newt = random.randint(1, 100)
                    blocks.append(newo)
                    game(blocks, score, diff)
            else:
                inc = useone + usetwo
                score -= 10
                print("That's not quite right,", useone, "+", usetwo, "=", inc, '\n', "Your current score is:", score)
                move = True
                game(blocks, score, diff)
        else:
            print("one or more of the numbers are not available ! Please try a differnet number")

def multiplication(blocks, score, diff):
    move = False
    while move != True:
        print("Your starting numbers are", blocks)
        valuone = random.randint(1, 15)
        valutwo = random.randint(1, 15)
        answer = blocks[valuone] * blocks[valutwo]
        print("? x ? =", answer)
        useone = int(input("Please enter your first value: "))
        usetwo = int(input("Please enter your second value: "))
        
        if useone and usetwo in blocks:
            if useone * usetwo == answer:
                score += 10
                blocks.remove(useone)
                blocks.remove(usetwo)
                print("That's correct !", '\n', "Your current score is:", score)
                move = True
                if diff == "easy":
                    newo = random.randint(1, 10)
                    newt = random.randint(1, 10)
                    blocks.append(newo)
                    blocks.append(newt)
                    multiplication(blocks, score, diff)
                if diff == "medium":
                    newo = random.randint(1, 50)
                    newt = random.randint(1, 50)
                    blocks.append(newo)
                    blocks.append(newt)
                    multiplication(blocks, score, diff)
                else:
                    newo = random.randint(1, 100)
                    newt = random.randint(1, 100)
                    blocks.append(newo)
                    multiplication(blocks, score, diff)
            else:
                inc = useone * usetwo
                score -= 10
                print("That's not quite right,", useone, "x", usetwo, "=", inc, '\n', "Your current score is:", score)
                move = True
                multiplication(blocks, score, diff)
        else:
            print("one or more of the numbers are not available ! Please try a differnet number")

def division(blocks, score, diff):
    move = False
    while move != True:
        print("Your starting numbers are", blocks)
        valuone = random.randint(1, 15)
        valutwo = random.randint(1, 15)
        answer = blocks[valuone] / blocks[valutwo]
        print("? / ? =", answer)
        useone = int(input("Please enter your first value: "))
        usetwo = int(input("Please enter your second value: "))
        
        if useone and usetwo in blocks:
            if useone / usetwo == answer:
                score += 10
                blocks.remove(useone)
                blocks.remove(usetwo)
                print("That's correct !", '\n', "Your current score is:", score)
                move = True
                if diff == "easy":
                    newo = random.randint(1, 10)
                    newt = random.randint(1, 10)
                    blocks.append(newo)
                    blocks.append(newt)
                    division(blocks, score, diff)
                if diff == "medium":
                    newo = random.randint(1, 50)
                    newt = random.randint(1, 50)
                    blocks.append(newo)
                    blocks.append(newt)
                    division(blocks, score, diff)
                else:
                    newo = random.randint(1, 100)
                    newt = random.randint(1, 100)
                    blocks.append(newo)
                    division(blocks, score, diff)
            else:
                inc = useone / usetwo
                score -= 10
                print("That's not quite right,", useone, "/", usetwo, "=", inc, '\n', "Your current score is:", score)
                move = True
                division(blocks, score, diff)
        else:
            print("one or more of the numbers are not available ! Please try a differnet number")

def subtraction(blocks, score, diff):
    move = False
    while move != True:
        print("Your starting numbers are", blocks)
        valuone = random.randint(1, 15)
        valutwo = random.randint(1, 15)
        answer = blocks[valuone] - blocks[valutwo]
        print("? - ? =", answer)
        useone = int(input("Please enter your first value: "))
        usetwo = int(input("Please enter your second value: "))
        
        if useone and usetwo in blocks:
            if useone - usetwo == answer:
                score += 10
                blocks.remove(useone)
                blocks.remove(usetwo)
                print("That's correct !", '\n', "Your current score is:", score)
                move = True
                if diff == "easy":
                    newo = random.randint(1, 10)
                    newt = random.randint(1, 10)
                    blocks.append(newo)
                    blocks.append(newt)
                    subtraction(blocks, score, diff)
                if diff == "medium":
                    newo = random.randint(1, 50)
                    newt = random.randint(1, 50)
                    blocks.append(newo)
                    blocks.append(newt)
                    subtraction(blocks, score, diff)
                else:
                    newo = random.randint(1, 100)
                    newt = random.randint(1, 100)
                    blocks.append(newo)
                    subtraction(blocks, score, diff)
            else:
                inc = useone - usetwo
                score -= 10
                print("That's not quite right,", useone, "-", usetwo, "=", inc, '\n', "Your current score is:", score)
                move = True
                subtraction(blocks, score, diff)
        else:
            print("one or more of the numbers are not available ! Please try a differnet number")
        
        
GenerateEasy()
menu(diff)
    
    
