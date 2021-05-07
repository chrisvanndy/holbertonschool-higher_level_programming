#!/usr/bin/python3
""" Text indedtation functions takes in parameters and performs
    actions on a string based on certain characters
"""


def text_indentation(text):
    """ text_indentation takes in the string "text" and performs certain actions
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    new_str2 = ""
    new_str3 = ""

    text_list = text.split(". ")
    for bit in range(len(text_list)):
        if bit < len(text_list) - 1:
            new_str += text_list[bit] + '.\n\n'
        else:
            new_str += text_list[bit]

    text_list2 = new_str.split(": ")
    for bit in range(len(text_list2)):
        if bit < len(text_list2) - 1:
            new_str2 += text_list2[bit] + ':\n\n'
        else:
            new_str2 += text_list2[bit]

    text_list3 = new_str2.split("? ")
    for bit in range(len(text_list3)):
        if bit < len(text_list3) - 1:
            new_str3 += text_list3[bit] + '?\n\n'
        else:
            new_str3 += text_list3[bit]

    print("{}".format(new_str3), end="")
