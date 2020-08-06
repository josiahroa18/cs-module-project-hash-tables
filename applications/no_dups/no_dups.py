def no_dups(s):
    cache = {}
    words = s.split()

    for i in range(len(words)):
        if words[i] in cache:
            words[i] = None
        else:
            cache[words[i]] = True

    string = ' '.join(filter(None, words))
    return string




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))