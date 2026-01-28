import random

# Game setup
attempts = 6
names = random.choice(["January",   "February","March", "April", "May", "June", "July", "August", "September", "October", "November","December"]).strip().lower()
name_display = ["_" for _ in names]  # placeholder for letters

print("//------ Welcome to Hangman Game -----//")
print("Life lins:", attempts,)

print("The name has", len(names), "letters:")
print(" ".join(name_display))

# Game loop
while attempts > 0 and "_" in name_display:
    guess = input("\nEnter  a letter: ")
    
    if guess == names:  # correct full name
        name_display = list(names)
        break
    
    elif len(guess) == 1 and guess in names:
        # Reveal all positions of guessed letter
        for i, letter in enumerate(names):
            if letter == guess:
            
                print("\n")
                name_display[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Lives left:", attempts)
    
    print(" ".join(name_display))
  
   
          


# Game end
if "_" not in name_display:
    print("\nCongratulations! You guessed the name:", names)

    
else:
    print("Sorry you were Hunaged")
    print("\nGame over! The correct name was:", names)
  
