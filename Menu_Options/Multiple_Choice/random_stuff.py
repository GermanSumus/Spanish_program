import random

def randomize_choices(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))

        rand_set.add(choices[target])

    return list(rand_set)


def rand_word(word_list, length, answer=True, used_words=set()):
    """Returns a random word for a new question with an
       answer if answer=True and random english words for multiple choices
       if answer=False"""
    done = False

    while not done:

        random_row = random.randrange(length)
        row = word_list[random_row]
        spanish = row[0]
        english = row[1]

        if answer:
            if spanish not in used_words:
                used_words.add(spanish)

                done = True

                return spanish, english
            else:
                continue

        else:
            done = True

            return english
