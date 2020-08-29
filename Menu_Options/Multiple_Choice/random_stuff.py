import random

def randomize_choices(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))

        rand_set.add(choices[target])

    return list(rand_set)


def rand_word(word_list, length, spanish=True, used_words=set()):
    """Returns a random spanish word for a new question with an
       english answer if spanish=True and random english words for
       multiple choices if spanish=False"""
    done = False

    while not done:

        random_row = random.randrange(length)
        row = word_list[random_row]
        ES = row[0]
        EN = row[1]
        if spanish==True:
            if spanish not in used_words:
                used_words.add(ES)
                done = True
                return ES, EN
            else:
                continue
        if spanish==False:
            done = True
            return EN
