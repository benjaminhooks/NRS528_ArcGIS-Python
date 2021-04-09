#Type a sentence, and the function will count the amount of times each word appears in the sentence

words = input("Type a sentence: ")

def word_count(x):
    counts = dict()
    words = x.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(words))
