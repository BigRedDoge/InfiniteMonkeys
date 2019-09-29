# the phrase the monkeys are desperately trying to type
phrase = 'impossible'

#percentage for odds that a space will be selected
CHANCE = 15

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# needed if random letter generator picks > 1 spaces in a row
alphabet_no_space = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_size = int(26 / ((100 - CHANCE) / 100))

# -27 (-1 because array start at 0, -26 for 26 letters already inserted)
for space in range(alphabet_size - 27):
    alphabet.append(' ')

alphabet_original = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
