# hw_7_4
capitals = ["Washington", "London", "Paris", "Berlin", "Rome", "Madrid", "Ottawa", "Tokyo", "Beijing", "Moscow"];


selected_city = capitals[4].upper() ;

guessed_city = ['_' if char.isalpha() else char for char in selected_city];

attempts = 0
while '_' in guessed_city:
    print(" ".join(guessed_city));
    guess = input("Guess a letter: ").upper();

    if guess in selected_city:
        for i in range(len(selected_city)):
            if selected_city[i] == guess:
                guessed_city[i] = guess
    else:
        print("The letter does not exist in the capital.");

    attempts += 1

print("Congratulations! You guessed the city:", selected_city);
print("It took you", attempts, "attempts.");
