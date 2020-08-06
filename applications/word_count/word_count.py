def word_count(s):
    cache = {}
    s = s.lower()
    ignore = '":;,.-+=/\\|[{]}()*^&'
    for char in s:
        if char in ignore:
            s = s.replace(char, "")

    words = s.split()

    for word in words:
        if word in cache:
            cache[word] += 1
        elif word == '':
            continue
        else:
            cache[word] = 1

    return cache
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))