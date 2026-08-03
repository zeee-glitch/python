# a guessing game
secret_word = "python"

while True:
    guess = input("quess the programinf language we are using").lower()
    if guess == secret_word:
        print("you guessed the correct language!!!")
        break
    else:
        print("incorrect guess try again!!!")