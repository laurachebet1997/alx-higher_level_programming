#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence_length < 1:
        return None
    first_t = sentence_length, sentence[0]
    return(first_t)
   #print("Length: {:d} - First character: {}".format(sentence_length, first_t))
