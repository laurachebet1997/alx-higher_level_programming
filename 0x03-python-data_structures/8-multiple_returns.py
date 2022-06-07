#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence_length < 1:
        first_t = 0, None
        return(first_t)
    else:
        first_t = sentence_length, sentence[0]
        return(first_t)
