#!/urs/bin/python3
def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as text:
        print(text.read(), end="")
