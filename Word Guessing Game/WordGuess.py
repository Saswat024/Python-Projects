import random

name = input("What is your name? ")
print("Good Luck ! ", name)

words = [
    "mathematics",
    "science",
    "technology",
    "computer",
    "algorithm",
    "programming",
    "artificial",
    "intelligence",
    "machine",
    "learning",
    "data",
    "analysis",
    "statistics",
    "probability",
    "calculus",
    "geometry",
    "algebra",
    "physics",
    "chemistry",
    "biology",
    "astronomy",
    "research",
    "experiment",
    "hypothesis",
    "theory",
    "discovery",
    "innovation",
    "creativity",
    "knowledge",
    "wisdom",
    "education",
    "university",
    "professor",
    "student",
    "library",
    "laboratory",
    "microscope",
    "telescope",
    "equation",
    "formula",
]

word = random.choice(words)
attempts = len(word) + 5

print(f"Guess the characters. You have {attempts} attempts. Good Luck")

guesses = ''

while attempts > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    if failed == 0:
        print(f"\nYou guessed it right!! The word is {word}")
        break

    print()
    guess = input("Guess a character: ")
    guesses += guess
    

    if guess not in word:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")
        if attempts == 0: 
            print(f"You Loose. The word was {word}. Try again.") 
