def compress_string(chars):
    i = 0
    write = 0
    n = len(chars)

    while i < n:
        char = chars[i]
        count = 0

        while i < n and chars[i] == char:
            count += 1
            i += 1

        chars[write] = char
        write += 1

        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1

    return write



print(compress_string(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))