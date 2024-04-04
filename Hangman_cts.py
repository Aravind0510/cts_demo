#Main 
class Hangman:
        def _init_(self, words):
                self.words = words
                self.secret_word = random.choice(words)
                self.guessed_letters = set()
                self.attempts_left = 6


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


#Aravind

        def play(self):
                print("Welcome to Hangman!")
                while True:
                    print("\nAttempts left:", self.attempts_left)
                    self.display_word_progress()
                    guess = self.take_user_guess()
                    self.check_guess(guess)
                    if self.check_win_loss():
                        break


words = ["python", "hangman", "game", "programming", "computer", "keyboard"]
game = Hangman(words)
game.play()
