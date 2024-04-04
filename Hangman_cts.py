#Main 
#Andrew
def display_word_progress(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        print(display)

def check_guess(self, guess):
        if guess in self.guessed_letters:
            print("You already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        if guess not in self.secret_word:
            self.attempts_left -= 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")
#Deepak -- take user guess
#Abdullah handle win/loss Condition
