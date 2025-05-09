#In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.
import sys
import random
digits = list("0123456789")
random.shuffle(digits)
num_real = ''.join(digits[:3])
tries = 0
#num_real = "390"
#num_guessed = "000"

while tries < 10:
    #print("Hello")
    tries += 1
    print(f"This is your {tries} try")
    num_guessed = input("Enter your guess (3-digit number): ")

    ##case where number is correct
    if(num_real == num_guessed):
        print(f"your guess is correct, the number is: {num_real}")
        sys.exit()
    else:
        if(tries == 10):
            print(f"You lost, the number is {num_real}")
        else:
            #print(f"Incorrect, keep guessing, you have {10 - tries} tries left")
            #case where guess is incorrect but has a digit in the correct place
            clues = []
            for char in range(len(num_guessed)):
                if(num_guessed[char] == num_real[char]):
                    clues.append('Fermi')
                elif num_guessed[char] in num_real:
                    clues.append("Pico")
            
            if not clues:
               print("Bagels") 
            else:
                print(' '.join(sorted(clues)))

                        
    
    
    
