

def isAlienSorted(words, order):
    # Create a dictionary that maps each character to its index in the alien alphabet
    order_map = {char: index for index, char in enumerate(order)}

    # Compare each word with the next word
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        # Compare character by character
        for j in range(min(len(word1), len(word2))):
            if order_map[word1[j]] < order_map[word2[j]]:
                break  # word1 is correctly ordered before word2
            elif order_map[word1[j]] > order_map[word2[j]]:
                return False  # word1 should not be before word2

        # If we reach the end and word1 is longer than word2, it's incorrect
        if len(word1) > len(word2):
            return False

    return True