#Main 
#Andrew
def 
#Deepak -- take user guess
def take_user_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Invalid input. Please enter a single letter.")

#Abdullah handle win/loss Condition
