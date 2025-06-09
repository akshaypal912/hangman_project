import random
word_list =['python','hangman','developer','programming','algorithm','function','variable']
def chosen_word():
    return random.choice(word_list)
def display_word(word,guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("welcome to the hangman!")
    word = chosen_word()
    guessed_letters=set()
    attempts=max(6,len(word)+2)

    while attempts>0:
        print("\nword:",display_word(word,guessed_letters))
        guess=input("guess a letter:").lower()
        if not guess.isalpha() or len(guess)!=1:
            print("please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("you have already gueesd that letter!")
            continue
            
        guessed_letters.add(guess)
        if guess in word:
            print("correct")
            if all(letter in guessed_letters for letter in word):
                print("\ncongratulations! you have guessed the word:",word) 
                break
            else:
                attempts -=1
                print("wrong! Attempts left:", attempts)
        if attempts == 0:
            print("\nGame over! the word was the",word)

if __name__ == "__main__":
        hangman()

                

