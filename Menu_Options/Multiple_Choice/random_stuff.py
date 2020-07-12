import random

def randomize_choices(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))

        rand_set.add(choices[target])

    return list(rand_set)


def rand_row(word_list, question=True, used_words=set()):
    """Returns a random row for a new question with an
       answer if question=True and random spanish words for multiple choices
       if question=False"""
    done = False

    while not done:
        random_row = random.randrange(100)
        row = word_list[random_row]
        word = row[1]
        answer = row[4]

        if question:
            if word not in used_words:
                used_words.add(word)

                done = True

                return word, answer
            else:
                continue

        else:
            done = True

            return answer
