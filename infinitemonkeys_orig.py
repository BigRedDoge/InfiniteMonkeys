import src/characters as words
import random
import math
import time

NO_SPACES = True
SPACE_LIMIT = True

if NO_SPACES:
    alphabet = words.alphabet_no_space
else:
    if SPACE_LIMIT:
        alphabet = words.alphabet
    else:
        alphabet = words.alphabet_original

def main():
    iteration = 0
    output_file_name = 'shakespeare1.txt'
    time_start = time.time()

    while True:
        typing_interval = 250000
        check_interval = 1000000

        iteration += 1

        if iteration % typing_interval == 0:
            monkey_typing(typing_interval, output_file_name)

        if iteration % check_interval == 0:
            #print("Iteration: " + str(iteration))
            if iteration == check_interval:
                check, count = check_shakespeare(0, output_file_name)
            else:
                check, count = check_shakespeare(iteration - len(words.phrase) - check_interval, output_file_name)

            if check:
                print("Finished on iteration " + str(iteration))
                return "The Monkeys did it! It took " + str(count + (math.floor(iteration / 50000000))*50000000) + " letters to finally type it out.  Truely Shakespearian."

        if iteration % 100000 == 0:
            print("Iteration " + str(iteration))

        if iteration % 10000000 == 0:
            output_file_name = 'shakespeare' + str(int((iteration / 10000000) + 1)) + '.txt'
            print(output_file_name)

        if iteration % 25000000 == 0:
            print("Time Elapsed: " + str((time.time() - time_start)) + " Seconds")
            print("Iterations Completed: " + str(iteration))


def monkey_typing(interval, output_file):
    letter_chunk = []
    # checks to make sure there are no repeat spaces
    if NO_SPACES:
        for i in range(interval-1):
            letter_chunk.append(random_no_space())
    else:
        for i in range(interval-1):
            if i:
                if letter_chunk[i - 1] == ' ':
                    letter_chunk.append(random_no_space())
                else:
                    letter_chunk.append(random_letter())
            else:
                letter_chunk.append(random_letter())

    with open(output_file, 'a') as file:
        file.write(''.join(letter_chunk))


def check_shakespeare(iter, output_file):
    with open(output_file, 'r') as file:
        #file.seek(iter)
        last_written = file.read()
        check_for_phrase = last_written.find(words.phrase)
        if check_for_phrase != -1:
            return True, check_for_phrase
        else:
            return False, -1


def random_letter():
    rand_index = random.randrange(0, len(words.alphabet))
    letter = words.alphabet[rand_index]
    return letter


def random_no_space():
    rand_index = random.randrange(0, len(words.alphabet_no_space))
    letter = words.alphabet[rand_index]
    return letter


if __name__ == '__main__':
    print(main())
