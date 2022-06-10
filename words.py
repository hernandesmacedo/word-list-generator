def acronym(words: list):
    return ''.join([letter[0] for letter in words])

def large_words_acronym(words: list):
    return ''.join([word[0] if len(word) > 3 else '' for word in words])
