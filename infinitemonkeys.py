import math
import time
import sys

sys.path.insert(0, 'src')
from src import random_generator as rand_gen
from src import characters as chars

PHRASE = 'monkeys'
TYPE_INTERVAL = 250000
CHECK_INTERVAL = 1000000

NO_SPACES = False
SPACE_LIMIT = False

if NO_SPACES:
    alphabet = chars.alphabet_no_space
else:
    if SPACE_LIMIT:
        alphabet = chars.alphabet
    else:
        alphabet = chars.alphabet_original


def main():
    iteration = 0
    output_file_name = 'shakespeare1.txt'
    time_start = time.time()
    while True:

        iteration += 1

        if iteration % TYPE_INTERVAL == 0:
            monkey_typing(TYPE_INTERVAL, output_file_name)

        if iteration % CHECK_INTERVAL == 0:
            #print("Iteration: " + str(iteration))
            if iteration == CHECK_INTERVAL:
                check, count = check_shakespeare(0, output_file_name)
            else:
                check, count = check_shakespeare(iteration - len(PHRASE) - CHECK_INTERVAL, output_file_name)

            if check:
                print("Finished on iteration " + str(iteration))
                return "The Monkeys did it! It took " + str(count + (math.floor(iteration / 50000000))*50000000) + " letters to finally type it out.  Truely Shakespearian."

        if iteration % 100000 == 0:
            print("Iteration " + str(iteration))

        if iteration % 10000000 == 0:
            output_file_name = 'shakespeare' + str(int((iteration / 10000000) + 1)) + '.txt'
            print(output_file_name)

        if iteration % 2500000 == 0:
            print("Time Elapsed: " + str((time.time() - time_start)) + " Seconds")
            print("Iterations Completed: " + str(iteration))


def monkey_typing(interval, output_file):
    letter_chunk = []
    # checks to make sure there are no repeat spaces
    if NO_SPACES:
        for i in range(interval-1):
            letter_chunk.append(rand_gen.no_space())
    else:
        for i in range(interval-1):
            if i:
                if letter_chunk[i - 1] == ' ':
                    letter_chunk.append(rand_gen.no_space())
                else:
                    letter_chunk.append(rand_gen.letter())
            else:
                letter_chunk.append(rand_gen.letter())

    with open(output_file, 'a') as file:
        file.write(''.join(letter_chunk))


def check_shakespeare(iter, output_file):
    with open(output_file, 'r') as file:
        #file.seek(iter)
        last_written = file.read()
        check_for_phrase = last_written.find(PHRASE)
        if check_for_phrase != -1:
            return True, check_for_phrase
        else:
            return False, -1


if __name__ == '__main__':
    print(main())
