def multiple_returns(sentence):
    if not sentence:
        return 0, None
    
    length = len(sentence)
    first_character = sentence[0]

    return length, first_character