

def  get_word_count(filename):

    poem = open(filename)

    num_word = {}

    for line in poem:
        words = line.split()

        for word in words:
            num_word [word] = num_word.get(word, 0) + 1

    for word, count in num_word.items():
        print(word, count)

get_word_count("test.txt")
# get_word_count("twain.txt")

