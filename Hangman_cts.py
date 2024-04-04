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
 def check_win_loss(self):
        if all(letter in self.guessed_letters for letter in self.secret_word):
            print("Congratulations! You guessed the word:", self.secret_word)
            return True
        elif self.attempts_left == 0:
            print("Game over! The word was:", self.secret_word)
            return True
        return False
