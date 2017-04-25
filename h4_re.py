#!/usr/bin/python3
import random
import sys
import time

# ascII arts
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
E = '\033[33m'  # orange
EARTH = G + "(@)" + W
ROCKET = E + "\b-<#=#<" + W
END_OF_THE_WORLD = G + "(." + R + "\BOOM!/" + E + ",#<" + W


def on_cheat_mode(city):
    '''turns on cheat mode'''
    if sys.argv[1] == "demo":
        print(R + "\nGuessed letters:", *city, "<-- cheat mode ON" + W)


def handle_word_guess(city, guessed, lives):
    '''reads word,validate word, setting guessed or not,
    setting lives, returns guessed and Lives'''
    word = input("guess city: ").upper()
    if (word == city):  # quit from the "guessing loop"
        guessed = True  # (by condition checking)
    else:
        lives -= 2  # punishment
        print("You are wrong! ")
    return guessed, lives


def handle_letter_guess(city, guessed, lives, wrong, letters):
    '''reads letter, validate letter, setting guessed or not, setting
    lives, update "letteres" and "wrong", returns: guessed, lives,
    wrong, letters '''
    char = input("type a letter: ").upper()
    while len(char) < 2:
        if char in city:  # adding GOOD letter
            for i in range(0, len(city)):
                if (city[i] == char):
                    letters[i] = char
            break
        else:  # adding WRONG letter to list + punishment
            lives -= 1
            if char not in wrong:
                wrong.append(char)
            break
    else:
        print("Too many letters.")
    if (''.join(letters) == str(city)):  # quit from the "guessing loop"
        guessed = True  # (by condition checking)
    return guessed, lives, wrong, letters


def load_random_city():
    '''opens file, divides lines, randomises city and country'''
    with open('countries_and_capitals.txt', "r") as from_file:
        capitals_2 = from_file.read().splitlines()
    random_line = random.choice(capitals_2)
    country_and_capital = random_line.split(" | ")
    city = country_and_capital[1].upper()
    return city, country_and_capital


def main():

    print("\nYour mission is to save the world:", EARTH,
          "\nHurry up, lethal ROCKET: ", ROCKET, "is coming.")

    while True:  # main loop
        city, country_and_capital = load_random_city()
        letters = []
        wrong = []
        lives = 5
        count = 0
        guessed = False
        start_time = time.time()
        for i in city:
            letters.append('_')

        if (len(sys.argv) - 1):
            on_cheat_mode(city)  # cheat mode => display city name

        while (lives > 0 and not guessed):  # guessing loop
            if lives == 1:
                print("Hint: this is capital of",
                      country_and_capital[0].upper())
            print("\nLives:", lives, EARTH, (lives - 1) * " ", ROCKET,
                  "\nGuessed letters:", *letters, "  Wrong characters:",
                  *wrong)

            w_or_l = input("\n(W)ord or (L)etter: ").upper()
            # decision: word guessing, or another letter

            if (w_or_l == "W"):  # word guessing
                count += 1
                guessed, lives = handle_word_guess(city, guessed, lives)
            elif (w_or_l == "L"):  # letter guessing
                count += 1
                guessed, lives, wrong, letters = handle_letter_guess(city,
                                            guessed, lives, wrong, letters)

        if (guessed):
            guessing_time = round(time.time() - start_time)
            print(G + "\nCongratulations, you saved the world in", count,
                  "letters and", guessing_time, "seconds" + W)

        if (lives < 1):
            print(R + "\nYou are dead: ", END_OF_THE_WORLD)

        again = input("Thank you for playing. Enter Q\
                        to quit the program: ").upper()
        if again == 'Q':
            break


if __name__ == '__main__':
    main()
