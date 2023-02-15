import random

from termcolor import colored


def binary_search():
    while True:
        desired = int(input("give number: "))
        if desired < 1000 and desired > 0:
            break

    values = []
    for x in range(0, 101):
        values.append(random.randrange(0, 1000))
    print(values)
    values.sort()
    print(values)

    print("looking for " + str(desired))

    l = 0
    r = len(values) - 1
    c = 0

    while l <= r:
        c = (l + r) // 2
        if values[c] == desired:
            print("TRUE")
            return True
        elif values[c] < desired:
            l = c + 1
        elif values[c] > desired:
            r = c - 1

    print("FALSE")
    return False


def wordle():
    wordlist = ["apple", "tweak", "spans", "logos", "gland",
                "twice", "climb", "crash", "print", "zebra"]
    # process word list
    processed_word_list = {}
    for w in wordlist:
        processed_word_list[w] = get_char_table(w)

    # enter game loop
    while True:
        # init for turn
        selection = wordlist[random.randrange(0, len(wordlist))]
        turns = 0
        print("New word selected, good luck!")

        # enter guess loop
        while turns < 6:
            guess = input("Guess " + str(turns + 1)).lower()
            if validate_guess(selection, guess):
                print("Congratulations!, you win!")
                break
            else:
                turns += 1

        if turns >= 6:
            print('Sorry, the correct word was "' + selection + '".')

        # input validation loop to continue
        while True:
            prompt = input("Play again? (y/n)").lower()
            if prompt[0] == "y":
                break
            elif prompt[0] == "n":
                return
            else:
                print("Invalid input, try again.")


def validate_guess(selection, guess):
    char_counter = get_char_table(selection)
    g = [*guess]
    colored_string = ""

    # for each character
    for x in range(5):
        not_present = True
        # if we have an index list and its not empty
        if char_counter.get(g[x]) != None and char_counter[g[x]] != []:
            # iterate through the index list
            for i in range(len(char_counter[g[x]])):
                # if we have a hit, mark green and remove from index list
                if x == char_counter[g[x]][i]:
                    del char_counter[g[x]][i]
                    colored_string += colored(g[x], "green")
                    not_present = False
                    break
            # if not, mark yellow and take one away
            if len(char_counter[g[x]]) > 0 and not_present:
                char_counter[g[x]].pop()
                colored_string += colored(g[x], "yellow")
        else:
            colored_string += colored(g[x], "dark_grey")

    print(colored_string)
    return selection == guess


# given a word, yield a dictionary with letters as keys
# and values being the index in which the letter occurs
def get_char_table(word):
    w = [*word]
    result = {}
    for x in range(5):
        if result.get(w[x]) == None:
            result[w[x]] = [x]
        else:
            result[w[x]].append(x)
    return result


if __name__ == "__main__":
    binary_search()
    wordle()
