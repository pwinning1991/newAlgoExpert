def firstNonRepeatingCharacter(string):
    char_counts = {}
    for chr in string:
        char_counts[chr] = char_counts.get(chr, 0) + 1
    for idx in range(len(string)):
        if char_counts[string[idx]] == 1:
            return idx
    return -1