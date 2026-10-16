import random


def play_game(target=None, max_attempts=None):
    print("Welcome to the guessing game.")
    print("I'm thinking of a number between 1-100.")

    switch = True
    if max_attempts == None:
        max_attempts = 0
        switch = False

    if target == None:
        target = random.randint(1, 100)
    else:
        target = int(target)

    # print(target)

    while True:
        if switch and max_attempts == 0:
            print(f"You loose! the number is {target}")
            break

        try:
            user_num = int(input("What's your guess: "))
        except:
            print("invalid input. enter a whole number between 1 and 100.")
            continue

        if user_num > 100 or user_num < 1:
            print("invalid input! Enter a whole number between 1 and 100.")
            continue

        if switch and user_num == target:
            max_attempts -= 1
            print(f"correct! you had {max_attempts} guesses left")
            break
        elif not switch and user_num == target:
            max_attempts += 1
            print(f"correct! you got it in {max_attempts} guesses")
            break
        elif user_num > target:
            if switch:
                print("too high")
                max_attempts -= 1
                continue
            else:
                print("too high")
                max_attempts += 1
                continue
        else:
            if switch:
                print("too low")
                max_attempts -= 1
                continue
            else:
                print("too low")
                max_attempts += 1
                continue

    resume = input("Do you want to play again(Yes/No): ")
    if resume.lower() == "yes":
        play_game()
    elif resume.lower() == "no":
        print("Bye")
        return
    else:
        print("Invalid Input")
        return

# import random


# def play_game(target=None, max_attempts=None):
#     print("Welcome to the guessing game.")
#     print("I'm thinking of a number between 1-100.")
#     defined_max = True
#     if target is None:
#         target = random.randint(1, 100)
#     # print(target)
    
#     if max_attempts == None:
#         max_attempts = 1
#         defined_max = False
        
#     while True:
#         if defined_max and max_attempts == 0:
#             print(f"You lost, the number was {target}")
#             break

#         try:
#             user_num = int(input("What's your guess: "))
#         except:
#             print("invalid input. enter a whole number between 1 and 100.")
#             continue

#         if user_num > 100 or user_num < 1:
#             print(f"Invalid guess, please put a whole number between 1 and 100")
#             continue

#         if user_num > target:
#             print("Too high")
#             if not defined_max:
#                 max_attempts += 1
#             else:
#                 max_attempts -= 1
#                 print(f"You have {max_attempts} guesses left.")
#             continue
#         elif user_num < target:
#             print("Too Low")
#             if not defined_max:
#                 max_attempts += 1
#             else:
#                 max_attempts -= 1
#                 print(f"You have {max_attempts} guesses left.")
#             continue


#         if defined_max and user_num == target:
#             print(f"Correct! You got it and you still had {max_attempts} guesses left.")
#             break
#         elif not defined_max and user_num == target:
#             print(f"Correct! You got it in {max_attempts} guesses.")
#             break
        
#     res_game = input("Do you want to play again ('Yes', 'No')? ")
#     if res_game.lower() == "yes":
#         play_game()
#     elif res_game.lower() == "no":
#         print("Bye")
#         return

        


# Do not modify below this line
if __name__ == "__main__":
    play_game()
