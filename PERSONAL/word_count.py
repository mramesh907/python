def string_compression():
    s = input("Enter a string: ")
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    print(str(count))
    compressed.append(s[-1] + str(count))
    print("Compressed string:", ''.join(compressed))

string_compression()
