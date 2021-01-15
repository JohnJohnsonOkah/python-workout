"""
When given a list of words, this program displays the length
of the shortest and longest words and the average word length.
"""


def wordlength(*words):
    """
    This function takes in a list of words
    and return
    - the length of the shortest word
    - the length of the longest word
    - the average word length
    """

    shortest = len(words[0])
    longest = 0
    total = 0

    for word in words:
        wordlen = len(word)

        if wordlen < shortest:
            shortest = wordlen

        if wordlen > longest:
            longest = wordlen
        total += wordlen

    average = total / len(words)
    return (shortest, longest, average)


print(wordlength("my", "name", "is", "jjokah"))
