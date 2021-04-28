#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        firstchar = None
    else:
        firstchar = sentence[:1]
    return(length, firstchar)
