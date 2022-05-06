import random
from multiprocessing import Pool

POOL_SIZE = 32  # <1>

words_in = open('../DATA/words.txt')
WORDS = (w.strip() for w in words_in)  # <2>

# random.shuffle(WORDS)  # <3>


def my_task(word):  # <4>
    return word.upper()


if __name__ == '__main__':
    ppool = Pool(POOL_SIZE)  # <5>

    WORD_LIST = ppool.map(my_task, WORDS)  # <6>

    print(WORD_LIST[:20])  # <7>
    print()
    print(WORD_LIST[-20:])

    print("Processed {} words.".format(len(WORD_LIST)))

    words_in.close()