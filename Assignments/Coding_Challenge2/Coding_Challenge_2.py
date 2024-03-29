# Coding Challenge 2 - Ben Hooks

# 1. List Values

list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

print([int for int in list if int <5])


# 2. List overlap

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

def overlap(list_a, list_b):
        list_c = [value for value in list_a if value in list_b]
        return (list_c)

print(overlap(list_a, list_b))


def no_overlap(list_a, list_b):
    list_d = [value for value in list_a if not value in list_b]
    return (list_d)


print(no_overlap(list_a, list_b))


# 3. Word count

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count('hi dee hi how are you mr dee'))


# 4. User input

age = input("Retirement! Enter your age: ")
retirement = 65 - int(age)

print("Your age is " + str(age) + " " + "and you have " + str(retirement) + " " + "year(s) until retirement. ")

# 5.  User input 2


letter_scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

chosen_word = input('Scrabble! Enter word: ')
def scrabble_score(word):
    total = 0
    for i in word:
        total = total+letter_scores[i]
    return total

print("Your word score is" + " " + str(scrabble_score(chosen_word)))

