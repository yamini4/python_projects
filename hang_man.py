import random
import time
print("\nWelcome to hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello" + name + "!best of luck")
time.sleep(2)
print("the game is about to start !\n let's play hangman!")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["jeep", "border", "image", "film", "promise", "kid", "lung", "doll", "rhyme", "damage", "hen"]
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
def play_loop():
    global play_game
    play_game = input("do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("do you want to play again? y = yes, n = no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("thanks for playing! we expect you back again!")
            exit()
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("this is the hangman word: " + display + "enter yur guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid input, tr a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("try another letter.\n")
    else:
        count +=1
        if count == 1:
            time.sleep(1)
            print("   ________ \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "___|___\n")
            print("wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   ________ \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "___|___\n")
            print("wrong guess. " + str(limit -count) + "guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   ________ \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "__|__\n")
            print("wrong guess. " + str(limit - count) + "guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   ______ \n"
                  "   |     | \n"
                  "   |     |\n"
                  "   |     | \n"
                  "   |     0 \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("    ______ \n"
                  "   |      | \n"
                  "   |      |\n"
                  "   |      | \n"
                  "   |      0 \n"
                  "   |     /|\ \n"
                  "   |     / \ \n"
                  "___|___\n")
            print("wrong guess. you are hanged!!!\n")
            print("the word was:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print("congrats! you have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()




