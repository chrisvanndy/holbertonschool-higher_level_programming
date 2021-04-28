#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    drlen = len(dir(hidden_4))
    for i in range(drlen):
        names = dir(hidden_4)[i]
        if names.startswith("__"):
            continue
        print("{}".format(names))
